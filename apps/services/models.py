# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from apps.utils.managers import PublishedManager

class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название услуги')
    description =  models.TextField(verbose_name = u'описание')
    result =  models.TextField(verbose_name = u'результат')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'service_item')
        verbose_name_plural = _(u'service_items')

    def get_works(self):
        return self.document_set.published()

class Document(models.Model):
    service = models.ForeignKey(Service,verbose_name = u'услуга')
    description =  models.TextField(verbose_name = u'описание')
    is_link = models.BooleanField(verbose_name=u'документ можно получить на сайте', default=False)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'document')
        verbose_name_plural = _(u'documents')

class BlackList(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=u'Ф.И.О.')
    email = models.EmailField(verbose_name=u'электронная почта')
    phonenumber = models.CharField(max_length=100, verbose_name=u'номер телефона')

    def __unicode__(self):
        return self.full_name

    class Meta:
        ordering = ['-full_name']
        verbose_name = _(u'bl_subject')
        verbose_name_plural = _(u'bl_subjects')