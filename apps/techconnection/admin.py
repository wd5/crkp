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
    actions=['really_delete_selected']

    def get_actions(self, request):
        actions = super(ElectroloadAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            if obj.id != 7:
                obj.delete()

        message_bit = u"%s электропотребителя было" % queryset.count()
        self.message_user(request, u"%s успешно удалёно." % message_bit)
    really_delete_selected.short_description = u"Удалить выбранные электропотребители"

class MapPolygonAdminForm(forms.ModelForm):
    table_rates = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'таблица ставок',
    )
    class Meta:
        model = MapPolygon

class MapPolygonAdmin(admin.ModelAdmin):
    list_display = ('number', 'title','is_published',)
    list_display_links = ('number', 'title',)
    search_fields = ('number', 'table_rates',)
    list_editable = ('is_published',)

    form = MapPolygonAdminForm

admin.site.register(Electroload, ElectroloadAdmin)
admin.site.register(MapPolygon, MapPolygonAdmin)