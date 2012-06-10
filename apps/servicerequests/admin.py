# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.services.models import Service
from apps.servicerequests.models import TypicalRequest, BlackList
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

admin.site.register(TypicalRequest, TypicalRequestAdmin)
admin.site.register(BlackList, BlackListAdmin)


  