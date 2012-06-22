# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Question#,QuestionCategory
from django import forms
from apps.utils.widgets import Redactor, AdminImageWidget

class QuestionAdminForm(forms.ModelForm):
    answer = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Ответ',
    )
    class Meta:
        model = Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','pub_date','email', 'is_published',)
    list_display_links = ('id','pub_date',)
    list_editable = ('is_published',)
    search_fields = ('email', 'question', 'answer',)
    list_filter = ('pub_date','is_published',)
    fields = ('pub_date', 'email', 'question', 'answer', 'send_answer', 'is_published',)
    form = QuestionAdminForm

#class QuestionCategoryAdmin(admin.ModelAdmin):
#    list_display = ('title', 'order','is_published',)
#    list_display_links = ('title',)
#    list_editable = ('order','is_published',)

admin.site.register(Question, QuestionAdmin)
#admin.site.register(QuestionCategory, QuestionCategoryAdmin)