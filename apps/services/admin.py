# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.services.models import Service, Document, BlackList
from apps.utils.widgets import Redactor, AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

class DocumentsAdminForm(forms.ModelForm):
    description = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Описание',
    )
    class Meta:
        model = Document

    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/set_doc_height.js'
            )

class DocumentsAdminInline(admin.TabularInline):
    model = Document
    #form = DocumentsAdminForm
    extra = 0

class ServiceAdminForm(forms.ModelForm):
    result = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Результат',
    )
    class Meta:
        model = Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_published',)
    list_display_links = ('id', 'title',)
    list_editable = ('is_published', 'order',)
    form = ServiceAdminForm
    search_fields = ('title', 'description','result',)
    inlines = [
        DocumentsAdminInline,
    ]

class BlackListAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phonenumber',)
    list_display_links = ('id', 'full_name', 'email', 'phonenumber',)
    search_fields = ('full_name', 'email', 'phonenumber',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(BlackList, BlackListAdmin)


  