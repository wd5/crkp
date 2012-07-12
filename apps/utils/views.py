# -*- coding: utf-8 -*-
import Image, ImageEnhance
from math import asin,sqrt,degrees

from django.conf import settings

def reduce_opacity(img, opacity):   
    """Returns an image with reduced opacity."""
    
    assert opacity >= 0 and opacity <= 1
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    else:
        img = img.copy()
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    img.putalpha(alpha)
    
    return img

def watermark(img, mark_img = settings.MARK_IMG_S, position = 'over', opacity = 0.6):
    PADDING = 10
    """Adds a watermark to an image."""

    img = Image.open(img)
    mark = Image.open(mark_img)
    
    img_w_p = img.size[0] - PADDING
    if img_w_p < mark.size[0]:
        ratio = float(img_w_p) / mark.size[0]
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
    
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # create a transparent layer the size of the image and draw the watermark in that layer.
    layer = Image.new('RGBA', img.size, (0,0,0,0))
    
    if position == 'over':
        for y in xrange(0, img.size[1], mark.size[1]):
            for x in xrange(0, img.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'title':
        # title, but preserve the aspect ratio
        ratio = min(float(img.size[0]) / mark.size[0], float(img.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        #layer.paste(mark, ((img.size[0] - w) / 2, (img.size[1] - h) / 2))
        layer.paste(mark, ((img.size[0] - w) / 2, 0))
    elif position == 'top-left':
        position = (PADDING, PADDING)
        layer.paste(mark, position)
    elif position == 'top-right':
        position = (img.size[0] - mark.size[0] - PADDING, PADDING)
        layer.paste(mark, position)
    elif position == 'center':
        position = ((img.size[0] - mark.size[0])/2, (img.size[1] - mark.size[1])/2)
        layer.paste(mark, position)
    elif position == 'bottom-left':
        position = (PADDING, img.size[1] - mark.size[1]  -PADDING,)
        layer.paste(mark, position)
    elif position == 'cross':
        # находим угол поворота
        c = sqrt(img.size[0]**2+img.size[1]**2)
        sinA = img.size[1]/c
        angle = degrees(asin(sinA))
        # поворачиваем
        mark = mark.rotate(angle, expand=True)
        # определяем размер и вставляем
        ratio = min(float(img.size[0]) / mark.size[0], float(img.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, ((img.size[0] - w) / 2, (img.size[1] - h) / 2))
    else: # 'bottom-right' (default)
        position = (img.size[0] - mark.size[0] - PADDING, img.size[1] - mark.size[1] - PADDING,)
        layer.paste(mark, position)
        
    return Image.composite(layer, img, layer)