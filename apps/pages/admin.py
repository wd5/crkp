# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.pages.models import Page, MetaData, PageDoc, PagePic, Vacancy, License, LicensesCategory
from apps.utils.widgets import Redactor, AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe

class PageDocInline(admin.TabularInline):
    model = PageDoc
    sortable_field_name = 'order'
    extra = 0

class PagePicInlineForm(forms.ModelForm):
    file = forms.ImageField(label=u'Картинка', widget=AdminImageWidget)

class PagePicInline(AdminImageMixin, admin.TabularInline):
    model = PagePic
    form = PagePicInlineForm
    sortable_field_name = 'order'
    extra = 0

class PageAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Текст',
    )
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Page.objects\
            .exclude(id__exact=self.instance.pk).filter(parent = None)
    class Meta:
        model = Page

class PageAdmin(AdminImageMixin, MPTTModelAdmin):
    list_display = ('title', 'url', 'order', 'is_published',)
    list_display_links = ('title', 'url',)
    list_editable = ('is_published', 'order',)
    search_fields = ('title', 'url','content',)
    form = PageAdminForm

    #prepopulated_fields = {'slug': ('title',)}
    list_select_related = True
    form = PageAdminForm
    inlines = [
        #PageDocInline,
        #PagePicInline,
    ]

class MetaDataAdmin(admin.ModelAdmin):
    list_display=('url', 'title',)
    search_fields=('url','title',)


class VacancyAdminForm(forms.ModelForm):
    description = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Текст',
    )
    class Meta:
        model = Vacancy

class LicenseCategoryAdmin(AdminImageMixin,admin.ModelAdmin):
    list_display = ('id','title','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)

class LicenseAdmin(AdminImageMixin,admin.ModelAdmin):
    list_display = ('id','lic_title','order','is_published',)
    list_display_links = ('id','lic_title',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_published',)
    list_display_links = ('id', 'title',)
    list_editable = ('is_published', 'order',)
    search_fields = ('title', 'description',)

    form = VacancyAdminForm

admin.site.register(LicensesCategory, LicenseCategoryAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(Page, PageAdmin)


