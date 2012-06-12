# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.services.models import Service
from apps.servicerequests.models import TypicalRequest, BlackList, Reception, FirstServRequest, SecondServRequest
from apps.utils.widgets import Redactor, AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin
from apps.utils.customfilterspec import CustomFilterSpec

class BlackListAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phonenumber',)
    list_display_links = ('id', 'full_name', 'email', 'phonenumber',)
    search_fields = ('full_name', 'email', 'phonenumber',)

class TypicalRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'full_name', 'date_create',)
    list_display_links = ('id', 'full_name', 'date_create',)
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
            'fields': (('passport_series', 'passport_number',), 'passport_issued', 'passport_issued_date', 'inn',)
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': (('actual_address_with_index', 'object_title'),'object_location',)
        }),
        ('Параметры электроснабжения', {
            'classes': ('collapse',),
            'fields': (('earlier_power_kVA', 'additional_power','max_power',), 'earlier_power_kVt',)
        }),
        ('Другая информация', {
            'classes': ('collapse',),
            'fields': ('other_inf','date_create',)
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
            'fields': (('passport_series', 'passport_number',), 'passport_issued', 'passport_issued_date', 'inn',)
        }),
        ('Объект', {
            'classes': ('collapse',),
            'fields': (('actual_address_with_index', 'object_title'),'object_location','temp_period', )
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

class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phonenumber', 'date_create',)
    list_display_links = ('id', 'full_name', 'phonenumber', 'date_create',)
    search_fields = ('first_name', 'middle_name', 'last_name', 'phonenumber',)
    readonly_fields = ('date_create',)
    list_filter = ('date_create',)

    inlines = [
        FirstServRequestInline,
        SecondServRequestInline,
    ]

#class FirstServRequestAdmin(admin.ModelAdmin):
#    list_display = ('id', 'date_create',)
#    list_display = ('id', 'date_create',)
#    form = FirstServRequestForm
#    fieldsets = (
#        (None, {
#            'fields': ('connection_request', 'generated_pdf', ('last_name', 'first_name','middle_name'))
#        }),
#        ('Реквизиты', {
#            'classes': ('collapse',),
#            'fields': (('passport_series', 'passport_number',), 'passport_issued', 'passport_issued_date', 'inn',)
#        }),
#        ('Объект', {
#            'classes': ('collapse',),
#            'fields': (('actual_address_with_index', 'object_title'),'object_location',)
#        }),
#        ('Параметры электроснабжения', {
#            'classes': ('collapse',),
#            'fields': (('earlier_power_kVA', 'additional_power','max_power',), 'earlier_power_kVt',)
#        }),
#        (None, {
#            'fields': ('other_inf','date_create',)
#        }),
#    )
#    readonly_fields = ('date_create',)
#admin.site.register(FirstServRequest, FirstServRequestAdmin)
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

admin.site.register(TypicalRequest, TypicalRequestAdmin)
admin.site.register(BlackList, BlackListAdmin)
admin.site.register(Reception, ReceptionAdmin)


  