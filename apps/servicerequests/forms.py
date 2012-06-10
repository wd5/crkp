# -*- coding: utf-8 -*-
from django import forms
from apps.servicerequests.models import TypicalRequest

class TypicalRequestForm(forms.ModelForm):
    full_name = forms.CharField(
        required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(),
        required=True
    )
    phonenumber = forms.CharField(
        required=True
    )

    class Meta:
        model = TypicalRequest
        exclude = ('date_create',)

#class FirstServRequestForm(forms.ModelForm):
