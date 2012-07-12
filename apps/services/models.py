# -*- coding: utf-8 -*-
from django.db import models
import datetime, os
from django.db.models.signals import post_save
from apps.utils.utils import ImageField
from django.utils.translation import ugettext_lazy as _
from apps.utils.managers import PublishedManager
from pytils.translit import translify

class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название услуги')
    description =  models.TextField(verbose_name = u'описание')
    result =  models.TextField(verbose_name = u'результат')
    button_title = models.CharField(max_length=50, verbose_name=u'подпись кнопки')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    second_menu_blck = models.BooleanField(verbose_name=u'во втором блоке меню', default=False)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'service_item')
        verbose_name_plural = _(u'service_items')

    def get_published_docs(self):
        return self.document_set.published()

    def get_docs_zl(self):
        return self.document_set.published().filter(is_link=True)

    def get_docs_zs(self):
        return self.document_set.published().exclude(is_link=True)

    def get_absolute_url(self):
        return u'/services/%s/' % self.id

class Document(models.Model):
    service = models.ForeignKey(Service,verbose_name = u'услуга')
    description =  models.TextField(verbose_name = u'описание')
    is_link = models.BooleanField(verbose_name=u'есть ссылка для документа', default=False)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'документ для услуги №%s "%s..."' % (self.service.id,self.service.title[:40])

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'document')
        verbose_name_plural = _(u'documents')

    def doc_title(self):
        return u'документ для услуги №%s "%s..."' % (self.service.id,self.service.title[:40])
    doc_title.allow_tags = True
    doc_title.short_description = 'Название'

    def get_images(self):
        return self.documentimage_set.all()

def file_path_Documents_Images(instance, filename):
    return os.path.join('images','DocImages',  translify(filename).replace(' ', '_') )

class DocumentImage(models.Model):
    document = models.ForeignKey(Document, verbose_name=u'документ')
    image = ImageField(upload_to=file_path_Documents_Images, verbose_name=u'изображение')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)

    def __unicode__(self):
        return u'изображение к документу №%s' % self.document.id

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'doc_image')
        verbose_name_plural = _(u'doc_images')

    def get_src_image(self):
        return self.image.url

def watermark(sender, instance, created, **kwargs):
    from apps.utils.views import watermark
    from django.conf import settings
    path = "%s%s" % (settings.ROOT_PATH, instance.image.url)
    try:
        watermark(path,settings.MARK_IMG_S,'cross',opacity=0.1).save(path,quality=100)
    except:
        pass

post_save.connect(watermark, sender=DocumentImage)