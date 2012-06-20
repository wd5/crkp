# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.services.models import Service, Document
from apps.utils.widgets import Redactor

class DocumentsAdminForm(forms.ModelForm):
    description = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Описание',
    )
    class Meta:
        model = Document

#    class Media:
#        js = (
#            '/media/js/jquery.js',
#            )

#class DocumentsAdminInline(admin.TabularInline):
#    model = Document
#    #form = DocumentsAdminForm
#    extra = 0


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_title', 'is_link', 'order', 'is_published',)
    list_display_links = ('id', 'doc_title', )
    list_editable = ('is_published', 'order','is_link')
    search_fields = ('description',)
    list_filter = ('service',)
    form = DocumentsAdminForm

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
#    inlines = [
#        DocumentsAdminInline,
#    ]

admin.site.register(Document, DocumentsAdmin)
admin.site.register(Service, ServiceAdmin)