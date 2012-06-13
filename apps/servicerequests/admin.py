# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.services.models import Service
from apps.servicerequests.models import TypicalRequest, BlackList, Reception, FirstServRequest, SecondServRequest, ThirdServRequest, FourthServRequest, FifthServRequest
from apps.utils.widgets import Redactor, AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin
from apps.utils.customfilterspec import CustomFilterSpec

class BlackListAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phonenumber',)
    list_display_links = ('id', 'full_name', 'email', 'phonenumber',)
    search_fields = ('full_name', 'email', 'phonenumber',)

class TypicalRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'full_name', 'date_create',)
    list_display_links = ('id','service', 'full_name', 'date_create',)
    search_fields = ('full_name', 'email', 'phonenumber',)
    readonly_fields = ('date_create','service')
    list_filter = ('service',)

    custom_filter_spec = {'service': Service.objects.exclude(pk__in=[1,2,3,4,5])}

class FirstServRequestForm(forms.ModelForm):
    passport_issued = forms.CharField(widget=forms.Textarea, label = u'Паспорт выдан',)
    actual_address_with_index = forms.CharField(widget=forms.Textarea, label = u'Фактический адрес заявителя с индексом',)
    object_location = forms.CharField(widget=forms.Textarea, label = u'Местонахождение присоединяемого объекта',)

    class Meta:
        model = FirstServRequest

class FirstServRequestInline(admin.StackedInline):
    model = FirstServRequest
    form = FirstServRequestForm
    fieldsets = (
        (None, {
            'fields': ('generated_pdf', ('last_name', 'first_name','middle_name'))
        }),
        ('Реквизиты', {
            'classes': ('collapse',),
            'fields': (('passport_series', 'passport_number',), 'passport_issued', 'passport_issued_date', 'inn','actual_address_with_index',)
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': ('object_title', 'object_location')
        }),
        ('Параметры электроснабжения', {
            'classes': ('collapse',),
            'fields': (('earlier_power_kVA', 'additional_power','max_power',), 'earlier_power_kVt',)
        }),
        ('Другая информация', {
            'classes': ('collapse',),
            'fields': ('other_inf','agent_full_name',('authority_number','authority_date'),'phone_number','fax','email','date_create',)
        }),
        ('Приложения к заявке', {
            'classes': ('collapse',),
            'fields': ('req_attachment1','req_attachment2','req_attachment3','req_attachment4','req_attachment5',
                       'req_attachment6','req_attachment7','req_attachment8','req_attachment9',)
        }),
    )
    readonly_fields = ('date_create',)

class SecondServRequestForm(forms.ModelForm):
    passport_issued = forms.CharField(widget=forms.Textarea, label = u'Паспорт выдан',)
    actual_address_with_index = forms.CharField(widget=forms.Textarea, label = u'Фактический адрес заявителя с индексом',)
    object_location = forms.CharField(widget=forms.Textarea, label = u'Местонахождение присоединяемого объекта',)

    class Meta:
        model = SecondServRequest

class SecondServRequestInline(admin.StackedInline):
    model = SecondServRequest
    form = SecondServRequestForm
    fieldsets = (
        (None, {
            'fields': ('generated_pdf', ('last_name', 'first_name','middle_name'))
        }),
        ('Реквизиты', {
            'classes': ('collapse',),
            'fields': (('passport_series', 'passport_number',), 'passport_issued', 'passport_issued_date', 'inn','actual_address_with_index',)
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': (('object_title','object_location'),'temp_period', )
        }),
        ('I категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
        }),
        ('II категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
        }),
        ('III категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
        }),
        ('Другая информация', {
            'classes': ('collapse',),
            'fields': ('load_type','other_inf','date_create',)
        }),
    )
    readonly_fields = ('date_create',)

class ThirdServRequestForm(forms.ModelForm):
    org_title = forms.CharField(widget=forms.Textarea, label = u'Полное наименование организации/индивидуального предпринимателя',)
    actual_address_with_index = forms.CharField(widget=forms.Textarea, label = u'Фактический адрес организации (заявителя) с индексом',)
    object_location = forms.CharField(widget=forms.Textarea, label = u'Местонахождение присоединяемого объекта',)

    class Meta:
        model = ThirdServRequest

class ThirdServRequestInline(admin.StackedInline):
    model = ThirdServRequest
    form = ThirdServRequestForm
    fieldsets = (
        (None, {
            'fields': ('generated_pdf', ('org_title', 'egrul_number'), 'actual_address_with_index', )
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': (('object_title','object_location'), 'temp_period', )
        }),
        ('I категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
        }),
        ('II категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
        }),
        ('III категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
        }),
        ('Другая информация', {
            'classes': ('collapse',),
            'fields': ('load_type','other_inf','date_create',)
        }),
    )
    readonly_fields = ('date_create',)

class FourthServRequestForm(forms.ModelForm):
    org_title = forms.CharField(widget=forms.Textarea, label = u'Полное наименование организации/индивидуального предпринимателя',)
    actual_address_with_index = forms.CharField(widget=forms.Textarea, label = u'Фактический адрес организации (заявителя) с индексом',)
    object_location = forms.CharField(widget=forms.Textarea, label = u'Местонахождение присоединяемого объекта',)

    class Meta:
        model = FourthServRequest

class FourthServRequestInline(admin.StackedInline):
    model = FourthServRequest
    form = FourthServRequestForm
    fieldsets = (
        (None, {
            'fields': ('generated_pdf', ('org_title', 'egrul_number'), 'egrul_date', 'actual_address_with_index', )
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': (('object_title','object_location'))
        }),
        ('I категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
        }),
        ('II категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
        }),
        ('III категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
        }),
        ('Характеристики объекта', {
            'classes': ('collapse',),
            'fields': ('count_conn_points','load_type','power_distribution',)
        }),
        ('Другая информация', {
            'classes': ('collapse',),
            'fields': ('other_inf','date_create',)
        }),
    )
    readonly_fields = ('date_create',)

class FifthServRequestForm(forms.ModelForm):
    org_title = forms.CharField(widget=forms.Textarea, label = u'Полное наименование организации/индивидуального предпринимателя',)
    actual_address_with_index = forms.CharField(widget=forms.Textarea, label = u'Фактический адрес организации (заявителя) с индексом',)
    object_location = forms.CharField(widget=forms.Textarea, label = u'Местонахождение присоединяемого объекта',)

    class Meta:
        model = FifthServRequest

class FifthServRequestInline(admin.StackedInline):
    model = FifthServRequest
    form = FifthServRequestForm
    fieldsets = (
        (None, {
            'fields': ('generated_pdf', ('org_title', 'egrul_number'), 'egrul_date', 'actual_address_with_index', )
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': (('object_title','object_location'))
        }),
        ('I категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
        }),
        ('II категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
        }),
        ('III категория надежности электроснабжения', {
            'classes': ('collapse',),
            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
        }),
        ('Характеристики объекта', {
            'classes': ('collapse',),
            'fields': (('cnt_pwr_transformers','cnt_pwr_generators'),
                       'count_conn_points',
                       'load_type',
                       ('tech_min_generators','tech_armor_consumer','tech_emergency_armor_consumer'),
                       'power_distribution',)
        }),
        ('Другая информация', {
            'classes': ('collapse',),
            'fields': ('other_inf','date_create',)
        }),
    )
    readonly_fields = ('date_create',)

class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phonenumber', 'date_create',)
    list_display_links = ('id', 'full_name', 'phonenumber', 'date_create',)
    search_fields = ('first_name', 'middle_name', 'last_name', 'phonenumber',)
    readonly_fields = ('date_create',)
    list_filter = ('date_create',)

    inlines = [
        FirstServRequestInline,
        SecondServRequestInline,
        ThirdServRequestInline,
        FourthServRequestInline,
        FifthServRequestInline,
    ]

class FirstServRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_create',)
    list_display = ('id', 'date_create',)
    form = FirstServRequestForm
    fieldsets = (
        (None, {
            'fields': ('generated_pdf', ('last_name', 'first_name','middle_name'))
        }),
        ('Реквизиты', {
            'classes': ('collapse',),
            'fields': (('passport_series', 'passport_number',), 'passport_issued', 'passport_issued_date', 'inn','actual_address_with_index',)
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': ('object_title', 'object_location')
        }),
        ('Параметры электроснабжения', {
            'classes': ('collapse',),
            'fields': (('earlier_power_kVA', 'additional_power','max_power',), 'earlier_power_kVt',)
        }),
        ('Другая информация', {
            'classes': ('collapse',),
            'fields': ('other_inf','agent_full_name',('authority_number','authority_date'),'phone_number','fax','email',)
        }),
        ('Приложения к заявке', {
            'classes': ('collapse',),
            'fields': ('req_attachment1','req_attachment2','req_attachment3','req_attachment4','req_attachment5',
                       'req_attachment6','req_attachment7','req_attachment8','req_attachment9',)
        }),
        (None, {
            'fields': ('date_create',)
        }),
    )
    readonly_fields = ('date_create',)
admin.site.register(FirstServRequest, FirstServRequestAdmin)
#
#class SecondServRequestAdmin(admin.ModelAdmin):
#    list_display = ('id', 'date_create',)
#    form = SecondServRequestForm
#    fieldsets = (
#        (None, {
#            'fields': ('generated_pdf', ('last_name', 'first_name','middle_name'))
#        }),
#        ('Реквизиты', {
#            'classes': ('collapse',),
#            'fields': (('passport_series', 'passport_number',), 'passport_issued', 'passport_issued_date', 'inn',)
#        }),
#        ('Объект', {
#            'classes': ('collapse',),
#            'fields': (('actual_address_with_index', 'object_title'),'object_location','temp_period', )
#        }),
#        ('I категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
#        }),
#        ('II категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
#        }),
#        ('III категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
#        }),
#        ('Другая информация', {
#            'classes': ('collapse',),
#            'fields': ('load_type','other_inf','date_create',)
#        }),
#    )
#    readonly_fields = ('date_create',)
#admin.site.register(SecondServRequest, SecondServRequestAdmin)

#class ThirdServRequestAdmin(admin.ModelAdmin):
#    list_display = ('id', 'date_create',)
#    form = ThirdServRequestForm
#    fieldsets = (
#        (None, {
#            'fields': ('generated_pdf', ('org_title', 'egrul_number'))
#        }),
#        ('Объект', {
#            'classes': ('collapse',),
#            'fields': (('actual_address_with_index', 'object_title'),'object_location','temp_period', )
#        }),
#        ('I категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
#        }),
#        ('II категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
#        }),
#        ('III категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
#        }),
#        ('Другая информация', {
#            'classes': ('collapse',),
#            'fields': ('load_type','other_inf','date_create',)
#        }),
#    )
#    readonly_fields = ('date_create',)
#admin.site.register(ThirdServRequest, ThirdServRequestAdmin)

#class FourthServRequestAdmin(admin.ModelAdmin):
#    list_display = ('id', 'date_create',)
#    form = FourthServRequestForm
#    fieldsets = (
#        (None, {
#            'fields': ('generated_pdf', ('org_title', 'egrul_number'), 'egrul_date', 'actual_address_with_index', )
#        }),
#        ('Объект', {
#            'classes': ('collapse',),
#            'fields': (('object_title','object_location'))
#        }),
#        ('I категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
#        }),
#        ('II категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
#        }),
#        ('III категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
#        }),
#        ('Характеристики объекта', {
#            'classes': ('collapse',),
#            'fields': ('count_conn_points','load_type','power_distribution',)
#        }),
#        ('Другая информация', {
#            'classes': ('collapse',),
#            'fields': ('other_inf','date_create',)
#        }),
#    )
#    readonly_fields = ('date_create',)
#admin.site.register(FourthServRequest, FourthServRequestAdmin)

#class FifthServRequestAdmin(admin.ModelAdmin):
#    list_display = ('id', 'date_create',)
#    form = FifthServRequestForm
#    fieldsets = (
#        (None, {
#            'fields': ('generated_pdf', ('org_title', 'egrul_number'), 'egrul_date', 'actual_address_with_index', )
#        }),
#        ('Объект', {
#            'classes': ('collapse',),
#            'fields': (('object_title','object_location'))
#        }),
#        ('I категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('first_earlier_power_kVA', 'first_additional_power','first_max_power',), 'first_earlier_power_kVt',)
#        }),
#        ('II категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('second_earlier_power_kVA', 'second_additional_power','second_max_power',), 'second_earlier_power_kVt',)
#        }),
#        ('III категория надежности электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('third_earlier_power_kVA', 'third_additional_power','third_max_power',), 'third_earlier_power_kVt',)
#        }),
#        ('Характеристики объекта', {
#            'classes': ('collapse',),
#            'fields': (('cnt_pwr_transformers','cnt_pwr_generators'),
#                       'count_conn_points',
#                       'load_type',
#                       ('tech_min_generators','tech_armor_consumer','tech_emergency_armor_consumer'),
#                       'power_distribution',)
#        }),
#        ('Другая информация', {
#            'classes': ('collapse',),
#            'fields': ('other_inf','date_create',)
#        }),
#    )
#    readonly_fields = ('date_create',)
#admin.site.register(FifthServRequest, FifthServRequestAdmin)



admin.site.register(TypicalRequest, TypicalRequestAdmin)
admin.site.register(BlackList, BlackListAdmin)
admin.site.register(Reception, ReceptionAdmin)


  