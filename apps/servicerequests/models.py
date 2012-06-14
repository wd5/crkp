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
    object_title = models.CharField(max_length=200, verbose_name=u'наименование присоединяемого объекта')
    object_location = models.CharField(max_length=255, verbose_name=u'местонахождение присоединяемого объекта')

    earlier_power_kVA = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВА', max_digits=10, decimal_places=2)
    earlier_power_kVt = models.DecimalField(verbose_name=u'ранее присоединенная мощность кВт', max_digits=10, decimal_places=2)
    additional_power = models.DecimalField(verbose_name=u'вновь присоединяемая мощность (дополнительная)', max_digits=10, decimal_places=2)
    max_power = models.DecimalField(verbose_name=u'максимальная мощность (всего с учетом присоединенной мощности)', max_digits=10, decimal_places=2)
    other_inf = models.TextField(verbose_name=u'прочая информация')

    agent_full_name = models.CharField(max_length=100, verbose_name=u'заявитель/представитель')
    authority_number = models.CharField(max_length=100, verbose_name=u'доверенность №')
    authority_date = models.CharField(max_length=50, verbose_name=u'дата доверенности')
    phone_number = models.CharField(max_length=100, verbose_name=u'телефон для связи')
    fax = models.CharField(max_length=100, verbose_name=u'факс')
    email = models.EmailField(verbose_name=u'e-mail')

    req_attachment1 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего право собственности или иное предусмотренное законом основание на объект капитального строительства и (или) земельный участок, на котором расположены (будут располагаться) объекты заявителя либо право собственности или иное предусмотренное законом основание на энергопринимающие устройства.', default=False, blank=True)
    req_attachment2 = models.BooleanField(verbose_name = u'План расположения энергопринимающих устройств, которые необходимо присоединить к электрическим сетям сетевой организации (ситуационный план с привязкой к существующим улицам).', default=False, blank=True)
    req_attachment3 = models.BooleanField(verbose_name = u'Копия паспорта.', default=False, blank=True)
    req_attachment4 = models.BooleanField(verbose_name = u'Копия свидетельства о постановке на налоговый учет (при наличии).', default=False, blank=True)
    req_attachment5 = models.BooleanField(verbose_name = u'Согласование собственника или иного законного владельца сетей (в случае опосредованного присоединения). В согласовании должно быть указано: точка присоединения, мощность, категория надёжности, характеристика ввода (однофазный, трёхфазный).', default=False, blank=True)
    req_attachment6 = models.BooleanField(verbose_name = u'Копия доверенности на право подачи заявки, оформленная в установленном порядке, подтверждающая полномочия представителя заявителя, подающего и получающего документы, в случае если заявка подается в сетевую организацию представителем или иные документы, подтверждающие полномочия представителя заявителя.', default=False, blank=True)
    req_attachment7 = models.BooleanField(verbose_name = u'Копия договора электроснабжения владельца мощности (первый и последний лист, приложения с указанием мощности в «кВА», категории надёжности, точки присоединения, дополнительное соглашение о продлении договора на текущий год).', default=False, blank=True)
    req_attachment8 = models.BooleanField(verbose_name = u'Копия акта о технологическом присоединении (справки на мощность).', default=False, blank=True)
    req_attachment9 = models.BooleanField(verbose_name = u'Копия акта разграничения балансовой принадлежностей сетей и эксплуатационной ответственности сторон.', default=False, blank=True)

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
    object_title = models.CharField(max_length=200, verbose_name=u'наименование присоединяемого объекта')
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

    agent_full_name = models.CharField(max_length=100, verbose_name=u'заявитель/представитель')
    authority_number = models.CharField(max_length=100, verbose_name=u'доверенность №')
    authority_date = models.CharField(max_length=50, verbose_name=u'дата доверенности')
    phone_number = models.CharField(max_length=100, verbose_name=u'телефон для связи')
    fax = models.CharField(max_length=100, verbose_name=u'факс')
    email = models.EmailField(verbose_name=u'e-mail')

    req_attachment1 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего право собственности или иное предусмотренное законом основание на объект капитального строительства и (или) земельный участок, на котором расположены (будут располагаться) объекты заявителя либо право собственности или иное предусмотренное законом основание на энергопринимающие устройства.', default=False, blank=True)
    req_attachment2 = models.BooleanField(verbose_name = u'План расположения энергопринимающих устройств, которые необходимо присоединить к электрическим сетям сетевой организации (ситуационный план с привязкой к существующим улицам).', default=False, blank=True)
    req_attachment3 = models.BooleanField(verbose_name = u'Копия паспорта.', default=False, blank=True)
    req_attachment4 = models.BooleanField(verbose_name = u'Копия свидетельства о постановке на налоговый учет (при наличии).', default=False, blank=True)
    req_attachment5 = models.BooleanField(verbose_name = u'Согласование собственника или иного законного владельца сетей (в случае опосредованного присоединения). В согласовании должно быть указано: точка присоединения, мощность, категория надёжности, характеристика ввода (однофазный, трёхфазный).', default=False, blank=True)
    req_attachment6 = models.BooleanField(verbose_name = u'Копия доверенности на право подачи заявки, оформленная в установленном порядке, подтверждающая полномочия представителя заявителя, подающего и получающего документы, в случае если заявка подается в сетевую организацию представителем или иные документы, подтверждающие полномочия представителя заявителя.', default=False, blank=True)
    req_attachment7 = models.BooleanField(verbose_name = u'Копия договора электроснабжения владельца мощности (первый и последний лист, приложения с указанием мощности в «кВА», категории надёжности, точки присоединения, дополнительное соглашение о продлении договора на текущий год).', default=False, blank=True)
    req_attachment8 = models.BooleanField(verbose_name = u'Копия акта о технологическом присоединении (справки на мощность).', default=False, blank=True)
    req_attachment9 = models.BooleanField(verbose_name = u'Копия акта разграничения балансовой принадлежностей сетей и эксплуатационной ответственности сторон.', default=False, blank=True)

    date_create = models.DateTimeField(verbose_name = u'дата создания', default=datetime.datetime.now)

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'second_serv_request')
        verbose_name_plural = _(u'second_serv_requests')

# типовая заявка на услугу для "Договор и технические условия на подключение к электрическим сетям" Юридические лица и индивидуальные предприниматели до 100 кВт (включительно)
class ThirdServRequest(models.Model):
    connection_request = models.OneToOneField(Reception, verbose_name=u'запись на приём', blank=True, null=True)
    generated_pdf = models.FileField(upload_to='uploads/files/guests/', verbose_name=u'сгенерированная заявка', blank=True,)

    org_title = models.TextField(verbose_name=u'полное наименование организации/индивидуального предпринимателя')
    egrul_number = models.CharField(max_length=255, verbose_name=u'номер записи в Едином государственном реестре юридических лиц/Едином государственном реестре индивидуальных предпринимателей')

    actual_address_with_index = models.CharField(max_length=255, verbose_name=u'фактический адрес организации (заявителя) с индексом')
    object_title = models.CharField(max_length=200, verbose_name=u'наименование присоединяемого объекта')
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

    load_type = models.TextField(verbose_name=u'характер нагрузки потребителя электрической энергии')
    other_inf = models.TextField(verbose_name=u'прочая информация')

    agent_full_name = models.CharField(max_length=100, verbose_name=u'заявитель/представитель')
    authority_number = models.CharField(max_length=100, verbose_name=u'доверенность №')
    authority_date = models.CharField(max_length=50, verbose_name=u'дата доверенности')
    phone_number = models.CharField(max_length=100, verbose_name=u'телефон для связи')
    fax = models.CharField(max_length=100, verbose_name=u'факс')
    email = models.EmailField(verbose_name=u'e-mail')

    director_post = models.CharField(max_length=100, verbose_name=u'Должность руководителя')
    director_full_name = models.CharField(max_length=100, verbose_name=u'ФИО руководителя')
    agent_inn = models.CharField(max_length=12, verbose_name=u'ИНН')
    agent_kpp = models.CharField(max_length=9, verbose_name=u'КПП')
    agent_bik = models.CharField(max_length=9, verbose_name=u'БИК')
    agent_bank_title = models.CharField(max_length=255, verbose_name=u'Наименование банка')
    agent_bank_account = models.CharField(max_length=20, verbose_name=u'Расчетный счёт')
    agent_correspond_account = models.CharField(max_length=20, verbose_name=u'Корреспондентский счет')

    req_attachment1 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего право собственности или иное предусмотренное законом основание на объект капитального строительства и (или) земельный участок, на котором расположены (будут располагаться) объекты заявителя либо право собственности или иное предусмотренное законом основание на энергопринимающие устройства.', default=False, blank=True)
    req_attachment2 = models.BooleanField(verbose_name = u'План расположения энергопринимающих устройств, которые необходимо присоединить к электрическим сетям сетевой организации (ситуационный план с привязкой к существующим улицам).', default=False, blank=True)
    req_attachment3 = models.BooleanField(verbose_name = u'Согласование собственника или иного законного владельца сетей (в случае опосредованного присоединения). В согласовании должно быть указано: точка присоединения, мощность, категория надёжности, характеристика ввода (однофазный, трёхфазный).', default=False, blank=True)
    req_attachment4 = models.BooleanField(verbose_name = u'Копия свидетельства (решения) о государственной регистрации и копия свидетельства о постановке на налоговый учет.', default=False, blank=True)
    req_attachment5 = models.BooleanField(verbose_name = u'Копия Устава (со всеми изменениями или последняя редакция), либо выкопировку из Устава, содержащую титульный лист, раздел общих положений, раздел об исполнительных органах организации)', default=False, blank=True)
    req_attachment6 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего полномочия руководителя организации', default=False, blank=True)
    req_attachment7 = models.BooleanField(verbose_name = u'Копия выписки из ЕГРЮЛ, выданной не более чем за 30 календарных дней до даты обращения заявителя', default=False, blank=True)
    req_attachment8 = models.BooleanField(verbose_name = u'Копия доверенности на право подачи заявки, оформленная в установленном порядке, подтверждающая полномочия представителя заявителя, подающего и получающего документы, в случае если заявка подается в сетевую организацию представителем или иные документы, подтверждающие полномочия представителя заявителя.', default=False, blank=True)
    req_attachment9 = models.BooleanField(verbose_name = u'Копия договора электроснабжения владельца мощности (первый и последний лист, приложения с указанием мощности в «кВА», категории надёжности, точки присоединения, дополнительное соглашение о продлении договора на текущий год).', default=False, blank=True)
    req_attachment10 = models.BooleanField(verbose_name = u'Копия акта о технологическом присоединении (справки на мощность).', default=False, blank=True)
    req_attachment11 = models.BooleanField(verbose_name = u'Копия акта разграничения балансовой принадлежностей сетей и эксплуатационной ответственности сторон.', default=False, blank=True)

    date_create = models.DateTimeField(verbose_name = u'дата создания', default=datetime.datetime.now)

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'third_serv_request')
        verbose_name_plural = _(u'third_serv_requests')

# типовая заявка на услугу для "Договор и технические условия на подключение к электрическим сетям" Юридические лица и индивидуальные предприниматели до 750 кВА (включительно)
class FourthServRequest(models.Model):
    connection_request = models.OneToOneField(Reception, verbose_name=u'запись на приём', blank=True, null=True)
    generated_pdf = models.FileField(upload_to='uploads/files/guests/', verbose_name=u'сгенерированная заявка', blank=True,)

    org_title = models.TextField(verbose_name=u'полное наименование организации/индивидуального предпринимателя')
    egrul_number = models.CharField(max_length=255, verbose_name=u'номер записи в Едином государственном реестре юридических лиц/Едином государственном реестре индивидуальных предпринимателей')
    egrul_date = models.CharField(max_length=150, verbose_name=u'дата внесения в реестр') # ????

    actual_address_with_index = models.CharField(max_length=255, verbose_name=u'фактический адрес организации (заявителя) с индексом')
    object_title = models.CharField(max_length=200, verbose_name=u'наименование присоединяемого объекта')
    object_location = models.CharField(max_length=255, verbose_name=u'местонахождение присоединяемого объекта')

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

    count_conn_points = models.CharField(max_length=255, verbose_name=u'количество точек присоединения с указанием технических параметров элементов энергопринимающих устройств')
    load_type = models.TextField(verbose_name=u'характер нагрузки потребителя электрической энергии (вид производственной деятельности)')
    power_distribution = models.CharField(max_length=255, verbose_name=u'Поэтапное распределение мощности, сроков ввода и сведения о категории надежности электроснабжения, при вводе энергопринимающих устройств по этапам и очередям')
    other_inf = models.TextField(verbose_name=u'прочая информация')

    agent_full_name = models.CharField(max_length=100, verbose_name=u'заявитель/представитель')
    authority_number = models.CharField(max_length=100, verbose_name=u'доверенность №')
    authority_date = models.CharField(max_length=50, verbose_name=u'дата доверенности')
    phone_number = models.CharField(max_length=100, verbose_name=u'телефон для связи')
    fax = models.CharField(max_length=100, verbose_name=u'факс')
    email = models.EmailField(verbose_name=u'e-mail')

    director_post = models.CharField(max_length=100, verbose_name=u'Должность руководителя')
    director_full_name = models.CharField(max_length=100, verbose_name=u'ФИО руководителя')

    agent_inn = models.CharField(max_length=12, verbose_name=u'ИНН')
    agent_kpp = models.CharField(max_length=9, verbose_name=u'КПП')
    agent_bik = models.CharField(max_length=9, verbose_name=u'БИК')
    agent_bank_title = models.CharField(max_length=255, verbose_name=u'Наименование банка')
    agent_bank_account = models.CharField(max_length=20, verbose_name=u'Расчетный счёт')
    agent_correspond_account = models.CharField(max_length=20, verbose_name=u'Корреспондентский счет')

    req_attachment1 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего право собственности или иное предусмотренное законом основание на объект капитального строительства и (или) земельный участок, на котором расположены (будут располагаться) объекты заявителя либо право собственности или иное предусмотренное законом основание на энергопринимающие устройства.', default=False, blank=True)
    req_attachment2 = models.BooleanField(verbose_name = u'План расположения энергопринимающих устройств, которые необходимо присоединить к электрическим сетям сетевой организации (ситуационный план с привязкой к существующим улицам).', default=False, blank=True)
    req_attachment3 = models.BooleanField(verbose_name = u'Согласование собственника или иного законного владельца сетей (в случае опосредованного присоединения). В согласовании должно быть указано: точка присоединения, мощность, категория надёжности, характеристика ввода (однофазный, трёхфазный).', default=False, blank=True)
    req_attachment4 = models.BooleanField(verbose_name = u'Копия свидетельства (решения) о государственной регистрации и копия свидетельства о постановке на налоговый учет.', default=False, blank=True)
    req_attachment5 = models.BooleanField(verbose_name = u'Копия Устава (со всеми изменениями или последняя редакция), либо выкопировку из Устава, содержащую титульный лист, раздел общих положений, раздел об исполнительных органах организации)', default=False, blank=True)
    req_attachment6 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего полномочия руководителя организации', default=False, blank=True)
    req_attachment7 = models.BooleanField(verbose_name = u'Копия выписки из ЕГРЮЛ, выданной не более чем за 30 календарных дней до даты обращения заявителя.', default=False, blank=True)
    req_attachment8 = models.BooleanField(verbose_name = u'Таблица расчета нагрузок в кВА и кВт на общее количество мощности (ранее присоединенная мощность + дополнительная мощность), с указанием категории надёжности, адреса и наименования объекта, выполненного проектной организацией, имеющей допуск СРО (с предоставлением копии допуска СРО), и заверенная печатью организации.', default=False, blank=True)
    req_attachment9 = models.BooleanField(verbose_name = u'Перечень и мощность энергопринимающих устройств, которые могут быть присоединены к устройствам противоаварийной автоматики.', default=False, blank=True)
    req_attachment10 = models.BooleanField(verbose_name = u'Копия доверенности на право подачи заявки, оформленная в установленном порядке, подтверждающая полномочия представителя заявителя, подающего и получающего документы, в случае если заявка подается в сетевую организацию представителем или иные документы, подтверждающие полномочия представителя заявителя.', default=False, blank=True)
    req_attachment11 = models.BooleanField(verbose_name = u'Копия договора электроснабжения владельца мощности (первый и последний лист, приложения с указанием мощности в «кВА», категории надёжности, точки присоединения, дополнительное соглашение о продлении договора на текущий год).', default=False, blank=True)
    req_attachment12 = models.BooleanField(verbose_name = u'Копия акта о технологическом присоединении (справки на мощность).', default=False, blank=True)
    req_attachment13 = models.BooleanField(verbose_name = u'Копия акта разграничения балансовой принадлежностей сетей и эксплуатационной ответственности сторон.', default=False, blank=True)

    date_create = models.DateTimeField(verbose_name = u'дата создания', default=datetime.datetime.now)

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'fourth_serv_request')
        verbose_name_plural = _(u'fourth_serv_requests')

# типовая заявка на услугу для "Договор и технические условия на подключение к электрическим сетям" Юридические лица и индивидуальные предприниматели свыше 750 кВА
class FifthServRequest(models.Model):
    connection_request = models.OneToOneField(Reception, verbose_name=u'запись на приём', blank=True, null=True)
    generated_pdf = models.FileField(upload_to='uploads/files/guests/', verbose_name=u'сгенерированная заявка', blank=True,)

    org_title = models.TextField(verbose_name=u'полное наименование организации/индивидуального предпринимателя')
    egrul_number = models.CharField(max_length=255, verbose_name=u'номер записи в Едином государственном реестре юридических лиц/Едином государственном реестре индивидуальных предпринимателей')
    egrul_date = models.CharField(max_length=150, verbose_name=u'дата внесения в реестр') # ????

    actual_address_with_index = models.CharField(max_length=255, verbose_name=u'фактический адрес организации (заявителя) с индексом')
    object_title = models.CharField(max_length=200, verbose_name=u'наименование присоединяемого объекта')
    object_location = models.CharField(max_length=255, verbose_name=u'местонахождение присоединяемого объекта')

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

    cnt_pwr_transformers = models.CharField(max_length=255, verbose_name=u'количество и мощность присоединяемых к сети трансформаторов')
    cnt_pwr_generators = models.CharField(max_length=255, verbose_name=u'количество и мощность присоединяемых к сети генераторов')

    count_conn_points = models.CharField(max_length=255, verbose_name=u'количество точек присоединения с указанием технических параметров элементов энергопринимающих устройств')
    load_type = models.TextField(verbose_name=u'характер нагрузки потребителя электрической энергии (для генераторов-возможная скорость набора или снижения нагрузки) и наличие нагрузок, искажающих форму кривой электрического тока и вызывающих нессиметрию напряжения в точках присоединения')

    tech_min_generators = models.CharField(max_length=255, verbose_name=u'величина и обоснование величины технологического минимума (для генераторов)')
    tech_armor_consumer = models.CharField(max_length=255, verbose_name=u'величина и обоснование величины технологической брони (для потребителей электрической энергии)')
    tech_emergency_armor_consumer = models.CharField(max_length=255, verbose_name=u'величина и обоснование величины аварийной брони (для потребителей электрической энергии)')

    power_distribution = models.CharField(max_length=255, verbose_name=u'поэтапное распределение мощности, сроков ввода и сведения о категории надежности электроснабжения, при вводе энергопринимающих устройств по этапам и очередям')
    other_inf = models.TextField(verbose_name=u'прочая информация')

    agent_full_name = models.CharField(max_length=100, verbose_name=u'заявитель/представитель')
    authority_number = models.CharField(max_length=100, verbose_name=u'доверенность №')
    authority_date = models.CharField(max_length=50, verbose_name=u'дата доверенности')
    phone_number = models.CharField(max_length=100, verbose_name=u'телефон для связи')
    fax = models.CharField(max_length=100, verbose_name=u'факс')
    email = models.EmailField(verbose_name=u'e-mail')

    director_post = models.CharField(max_length=100, verbose_name=u'Должность руководителя')
    director_full_name = models.CharField(max_length=100, verbose_name=u'ФИО руководителя')

    agent_inn = models.CharField(max_length=12, verbose_name=u'ИНН')
    agent_kpp = models.CharField(max_length=9, verbose_name=u'КПП')
    agent_bik = models.CharField(max_length=9, verbose_name=u'БИК')
    agent_bank_title = models.CharField(max_length=255, verbose_name=u'Наименование банка')
    agent_bank_account = models.CharField(max_length=20, verbose_name=u'Расчетный счёт')
    agent_correspond_account = models.CharField(max_length=20, verbose_name=u'Корреспондентский счет')

    req_attachment1 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего право собственности или иное предусмотренное законом основание на объект капитального строительства и (или) земельный участок, на котором расположены (будут располагаться) объекты заявителя либо право собственности или иное предусмотренное законом основание на энергопринимающие устройства.', default=False, blank=True)
    req_attachment2 = models.BooleanField(verbose_name = u'План расположения энергопринимающих устройств, которые необходимо присоединить к электрическим сетям сетевой организации (ситуационный план с привязкой к существующим улицам).', default=False, blank=True)
    req_attachment3 = models.BooleanField(verbose_name = u'Согласование собственника или иного законного владельца сетей (в случае опосредованного присоединения). В согласовании должно быть указано: точка присоединения, мощность, категория надёжности, характеристика ввода (однофазный, трёхфазный).', default=False, blank=True)
    req_attachment4 = models.BooleanField(verbose_name = u'Копия свидетельства (решения) о государственной регистрации и копия свидетельства о постановке на налоговый учет.', default=False, blank=True)
    req_attachment5 = models.BooleanField(verbose_name = u'Копия Устава (со всеми изменениями или последняя редакция), либо выкопировку из Устава, содержащую титульный лист, раздел общих положений, раздел об исполнительных органах организации)', default=False, blank=True)
    req_attachment6 = models.BooleanField(verbose_name = u'Копия документа, подтверждающего полномочия руководителя организации', default=False, blank=True)
    req_attachment7 = models.BooleanField(verbose_name = u'Копия выписки из ЕГРЮЛ, выданной не более чем за 30 календарных дней до даты обращения заявителя.', default=False, blank=True)
    req_attachment8 = models.BooleanField(verbose_name = u'Таблица расчета нагрузок в кВА и кВт на общее количество мощности (ранее присоединенная мощность + дополнительная мощность), с указанием категории надёжности, адреса и наименования объекта, выполненного проектной организацией, имеющей допуск СРО (с предоставлением копии допуска СРО), и заверенная печатью организации.', default=False, blank=True)
    req_attachment9 = models.BooleanField(verbose_name = u'Перечень и мощность энергопринимающих устройств, которые могут быть присоединены к устройствам противоаварийной автоматики.', default=False, blank=True)
    req_attachment10 = models.BooleanField(verbose_name = u'Копия доверенности на право подачи заявки, оформленная в установленном порядке, подтверждающая полномочия представителя заявителя, подающего и получающего документы, в случае если заявка подается в сетевую организацию представителем или иные документы, подтверждающие полномочия представителя заявителя.', default=False, blank=True)
    req_attachment11 = models.BooleanField(verbose_name = u'Копия договора электроснабжения владельца мощности (первый и последний лист, приложения с указанием мощности в «кВА», категории надёжности, точки присоединения, дополнительное соглашение о продлении договора на текущий год).', default=False, blank=True)
    req_attachment12 = models.BooleanField(verbose_name = u'Копия акта о технологическом присоединении (справки на мощность).', default=False, blank=True)
    req_attachment13 = models.BooleanField(verbose_name = u'Копия акта разграничения балансовой принадлежностей сетей и эксплуатационной ответственности сторон.', default=False, blank=True)

    date_create = models.DateTimeField(verbose_name = u'дата создания', default=datetime.datetime.now)

    def __unicode__(self):
        return u'#%s' % self.id

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'fifth_serv_request')
        verbose_name_plural = _(u'fifth_serv_requests')