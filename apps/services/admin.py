# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.services.models import Service, Document, BlackList, TypicalRequest
from apps.utils.widgets import Redactor, AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

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
#            '/media/js/set_doc_height.js'
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


admin.site.register(TypicalRequest, TypicalRequestAdmin)
admin.site.register(Document, DocumentsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(BlackList, BlackListAdmin)


  