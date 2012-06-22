# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from apps.utils.utils import ImageField
import datetime
import os
from pytils.translit import translify
from django.db.models.signals import post_save
from apps.utils.managers import PublishedManager
from mptt.models import MPTTModel, TreeForeignKey, TreeManager

type_choices = (
    (u'input',u'input'),
    (u'textarea',u'textarea'),
    (u'redactor',u'redactor'),
)

class Settings(models.Model):
    title = models.CharField(
        verbose_name = u'Название',
        max_length = 150,
    )
    name = models.CharField( 
        verbose_name = u'Служебное имя',
        max_length = 250,
    )
    value = models.TextField(
        verbose_name = u'Значение'
    )
    type = models.CharField(
        max_length=20,
        verbose_name=u'Тип значения',
        choices=type_choices
    )
    class Meta:
        verbose_name =_(u'site_setting')
        verbose_name_plural =_(u'site_settings')

    def __unicode__(self):
        return u'%s' % self.name

def image_path_main_teasers(instance, filename):
    return os.path.join('images','main_teasers', translify(filename).replace(' ', '_') )

class MainTeaser(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'заголовок')
    url = models.CharField(max_length=200, verbose_name=u'ссылка', help_text=u'Адрес страницы на латинице. Например, "/your_address/"')
    description =  models.CharField(max_length=255, verbose_name=u'описание')
    image = ImageField(upload_to=image_path_main_teasers, verbose_name=u'картинка')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-order']
        verbose_name =_(u'main_teaser')
        verbose_name_plural =_(u'main_teasers')

    def get_src_image(self):
        return self.image.url