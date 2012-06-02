# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.techconnection.models import Electroload, Parameter, MapPolygon
from apps.utils.widgets import Redactor, AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

class ParameterAdminForm(forms.ModelForm):
    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/set_parameter_count_type.js'
            )

class ParameterAdminInline(admin.TabularInline):
    model = Parameter
    form = ParameterAdminForm
    extra = 0

class ElectroloadAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_published',)
    list_display_links = ('id', 'title',)
    list_editable = ('is_published', 'order',)
    search_fields = ('title',)
    inlines = [
        ParameterAdminInline,
    ]

class MapPolygonAdminForm(forms.ModelForm):
    table_rates = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'таблица ставок',
    )
    class Meta:
        model = MapPolygon

class MapPolygonAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'polygon',)
    list_display_links = ('id', 'number', 'polygon',)
    search_fields = ('number', 'table_rates',)

admin.site.register(Electroload, ElectroloadAdmin)
admin.site.register(MapPolygon, MapPolygonAdmin)