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

# типовая заявка на услуги
class TypicalRequest(models.Model):
    service = models.ForeignKey(Service,verbose_name = u'услуга')
    full_name = models.CharField(max_length=255, verbose_name=u'Ф.И.О.')
    email = models.EmailField(verbose_name= u'электронная почта')
    phonenumber = models.CharField(max_length=100, verbose_name=u'номер телефона')
    date_create = models.DateTimeField(verbose_name = u'Дата', default=datetime.datetime.now)

    def __unicode__(self):
        return self.full_name

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'typical_request')
        verbose_name_plural = _(u'typical_requests')