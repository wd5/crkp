# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from apps.services.models import Service
from apps.utils.managers import PublishedManager

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

    service.custom_filter_spec = True

    def __unicode__(self):
        return self.full_name

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'typical_request')
        verbose_name_plural = _(u'typical_requests')

# заявка на услугу для "Договор и технические условия на подключение к электрическим сетям" ФЛ до 15 кВт
class FirstServRequest(models.Model):
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