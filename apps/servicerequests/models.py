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
        return u'типовая заявка от %s' % self.date_create

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'typical_request')
        verbose_name_plural = _(u'typical_requests')

# запись на приём
class Reception(models.Model):
    last_name = models.CharField(max_length=50, verbose_name=u'фамилия')
    first_name = models.CharField(max_length=50, verbose_name=u'имя')
    middle_name = models.CharField(max_length=50, verbose_name=u'отчество')
    phonenumber = models.CharField(max_length=100, verbose_name=u'номер телефона')
    reception_date = models.DateField(verbose_name=u'дата приёма')
    reception_time = models.TimeField(verbose_name=u'время')
    date_create = models.DateTimeField(verbose_name = u'дата добавления', default=datetime.datetime.now)

    def __unicode__(self):
        return u'запись на приём №%s' % self.id

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'reception_item')
        verbose_name_plural = _(u'reception_items')

    def full_name(self):
        return '<span>%s %s %s</span>' % (self.last_name,self.first_name, self.middle_name)
    full_name.allow_tags = True
    full_name.short_description = 'Ф.И.О.'

# типовая заявка на услугу для "Договор и технические условия на подключение к электрическим сетям" фл < 15 кВт
class FirstServRequest(models.Model):
    connection_request = models.OneToOneField(Reception, verbose_name=u'запись на приём', blank=True, null=True)
    generated_pdf = models.FileField(upload_to='uploads/files/guests/', verbose_name=u'сгенерированная заявка', blank=True,)
    last_name = models.CharField(max_length=50, verbose_name=u'фамилия')
    first_name = models.CharField(max_length=50, verbose_name=u'имя')
    middle_name = models.CharField(max_length=50, verbose_name=u'отчество')
    passport_series = models.CharField(max_length=4, verbose_name=u'серия паспорта')
    passport_number = models.CharField(max_length=6, verbose_name=u'номер паспорта')
    passport_issued = models.CharField(max_length=150, verbose_name=u'паспорт выдан')
    passport_issued_date = models.CharField(max_length=150, verbose_name=u'дата выдачи') # ????
    inn = models.CharField(max_length=12, verbose_name=u'ИНН')
    actual_address_with_index = models.CharField(max_length=255, verbose_name=u'фактический адрес заявителя с индексом')
    object_title = models.CharField(max_length=200, verbose_name=u'наименование объекта')
    object_location = models.CharField(max_length=255, verbose_name=u'местонахождение присоединяемого объекта')
    earlier_power_kVA = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВА', max_digits=10, decimal_places=2)
    earlier_power_kVt = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВт', max_digits=10, decimal_places=2)
    additional_power = models.DecimalField(verbose_name=u'вновь присоединяемая мощность (дополнительная)', max_digits=10, decimal_places=2)
    max_power = models.DecimalField(verbose_name=u'максимальная мощность (всего с учетом присоединенной мощности)', max_digits=10, decimal_places=2)
    other_inf = models.TextField(verbose_name=u'прочая информация')

    date_create = models.DateTimeField(verbose_name = u'дата создания', default=datetime.datetime.now)

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'first_serv_request')
        verbose_name_plural = _(u'first_serv_requests')

# типовая заявка на услугу для "Договор и технические условия на подключение к электрическим сетям" Физические лица до 100 кВт (включительно)
class SecondServRequest(models.Model):
    connection_request = models.OneToOneField(Reception, verbose_name=u'запись на приём', blank=True, null=True)
    generated_pdf = models.FileField(upload_to='uploads/files/guests/', verbose_name=u'сгенерированная заявка', blank=True,)
    last_name = models.CharField(max_length=50, verbose_name=u'фамилия')
    first_name = models.CharField(max_length=50, verbose_name=u'имя')
    middle_name = models.CharField(max_length=50, verbose_name=u'отчество')
    passport_series = models.CharField(max_length=4, verbose_name=u'серия паспорта')
    passport_number = models.CharField(max_length=6, verbose_name=u'номер паспорта')
    passport_issued = models.CharField(max_length=150, verbose_name=u'паспорт выдан')
    passport_issued_date = models.CharField(max_length=150, verbose_name=u'дата выдачи') # ????
    inn = models.CharField(max_length=12, verbose_name=u'ИНН')
    actual_address_with_index = models.CharField(max_length=255, verbose_name=u'фактический адрес заявителя с индексом')
    object_title = models.CharField(max_length=200, verbose_name=u'наименование объекта')
    object_location = models.CharField(max_length=255, verbose_name=u'местонахождение присоединяемого объекта')

    temp_period = models.CharField(max_length=255, verbose_name=u'срок временного присоединения')

    first_earlier_power_kVA = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВА', max_digits=10, decimal_places=2)
    first_earlier_power_kVt = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВт', max_digits=10, decimal_places=2)
    first_additional_power = models.DecimalField(verbose_name=u'вновь присоединяемая мощность (дополнительная)', max_digits=10, decimal_places=2)
    first_max_power = models.DecimalField(verbose_name=u'максимальная мощность (всего с учетом присоединенной мощности)', max_digits=10, decimal_places=2)

    second_earlier_power_kVA = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВА', max_digits=10, decimal_places=2)
    second_earlier_power_kVt = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВт', max_digits=10, decimal_places=2)
    second_additional_power = models.DecimalField(verbose_name=u'вновь присоединяемая мощность (дополнительная)', max_digits=10, decimal_places=2)
    second_max_power = models.DecimalField(verbose_name=u'максимальная мощность (всего с учетом присоединенной мощности)', max_digits=10, decimal_places=2)

    third_earlier_power_kVA = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВА', max_digits=10, decimal_places=2)
    third_earlier_power_kVt = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВт', max_digits=10, decimal_places=2)
    third_additional_power = models.DecimalField(verbose_name=u'вновь присоединяемая мощность (дополнительная)', max_digits=10, decimal_places=2)
    third_max_power = models.DecimalField(verbose_name=u'максимальная мощность (всего с учетом присоединенной мощности)', max_digits=10, decimal_places=2)

    load_type = models.CharField(max_length=255, verbose_name=u'характер нагрузки потребителя электрической энергии')

    other_inf = models.TextField(verbose_name=u'прочая информация')

    date_create = models.DateTimeField(verbose_name = u'дата создания', default=datetime.datetime.now)

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'second_serv_request')
        verbose_name_plural = _(u'second_serv_requests')