# -*- coding: utf-8 -*-
from django import forms
from apps.servicerequests.models import TypicalRequest, FirstServRequest, Reception, SecondServRequest

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


class FirstServRequestForm(forms.ModelForm):
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    passport_series = forms.CharField(required=True)
    passport_number = forms.CharField(required=True)
    passport_issued = forms.CharField(widget=forms.Textarea, required=True)
    passport_issued_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    inn = forms.CharField(required=True)
    actual_address_with_index = forms.CharField(widget=forms.Textarea, required=True)
    object_title = forms.CharField(required=True)
    object_location = forms.CharField(widget=forms.Textarea, required=True)
    earlier_power_kVA = forms.DecimalField(required=True)
    earlier_power_kVt = forms.DecimalField(required=True)
    additional_power = forms.DecimalField(required=True)
    max_power = forms.DecimalField(required=True)
    other_inf = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = FirstServRequest
        exclude = ('connection_request', 'generated_pdf', 'date_create',)

    def clean_passport_series(self):
        passport_series = self.cleaned_data['passport_series']
        try:
            integer = int(passport_series)
        except:
            integer = False

        if len(passport_series) != 4 or not integer:
            raise forms.ValidationError("Серия паспорта содержит 4 цифры (сейчас %s)"%len(passport_series))
        return passport_series

    def clean_passport_number(self):
        passport_number = self.cleaned_data['passport_number']
        try:
            integer = int(passport_number)
        except:
            integer = False

        if len(passport_number) != 6 or not integer:
            raise forms.ValidationError("Номер паспорта содержит 6 цифр (сейчас %s)"%len(passport_number))
        return passport_number

    def clean_inn(self):
        inn = self.cleaned_data['inn']
        try:
            integer = int(inn)
        except:
            integer = False

        if (len(inn) != 10 and len(inn) != 12) or not integer:
            raise forms.ValidationError("ИНН содержит 10 или 12 цифр (сейчас %s)"%len(inn))
        return inn

class SecondServRequestForm(forms.ModelForm):
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    passport_series = forms.CharField(required=True)
    passport_number = forms.CharField(required=True)
    passport_issued = forms.CharField(widget=forms.Textarea, required=True)
    passport_issued_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    inn = forms.CharField(required=True)
    actual_address_with_index = forms.CharField(widget=forms.Textarea, required=True)
    object_title = forms.CharField(required=True)
    object_location = forms.CharField(widget=forms.Textarea, required=True)

    temp_period = forms.CharField(required=True)

    first_earlier_power_kVA = forms.DecimalField(required=True)
    first_earlier_power_kVt = forms.DecimalField(required=True)
    first_additional_power = forms.DecimalField(required=True)
    first_max_power = forms.DecimalField(required=True)

    second_earlier_power_kVA = forms.DecimalField(required=True)
    second_earlier_power_kVt = forms.DecimalField(required=True)
    second_additional_power = forms.DecimalField(required=True)
    second_max_power = forms.DecimalField(required=True)

    third_earlier_power_kVA = forms.DecimalField(required=True)
    third_earlier_power_kVt = forms.DecimalField(required=True)
    third_additional_power = forms.DecimalField(required=True)
    third_max_power = forms.DecimalField(required=True)

    load_type = forms.CharField(widget=forms.Textarea, required=True)

    other_inf = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = SecondServRequest
        exclude = ('connection_request', 'generated_pdf', 'date_create',)

    def clean_passport_series(self):
        passport_series = self.cleaned_data['passport_series']
        try:
            integer = int(passport_series)
        except:
            integer = False

        if len(passport_series) != 4 or not integer:
            raise forms.ValidationError("Серия паспорта содержит 4 цифры (сейчас %s)"%len(passport_series))
        return passport_series

    def clean_passport_number(self):
        passport_number = self.cleaned_data['passport_number']
        try:
            integer = int(passport_number)
        except:
            integer = False

        if len(passport_number) != 6 or not integer:
            raise forms.ValidationError("Номер паспорта содержит 6 цифр (сейчас %s)"%len(passport_number))
        return passport_number

    def clean_inn(self):
        inn = self.cleaned_data['inn']
        try:
            integer = int(inn)
        except:
            integer = False

        if (len(inn) != 10 and len(inn) != 12) or not integer:
            raise forms.ValidationError("ИНН содержит 10 или 12 цифр (сейчас %s)"%len(inn))
        return inn

class ReceptionForm(forms.ModelForm):
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    phonenumber = forms.CharField(required=True)
    reception_date = forms.DateField(required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    reception_time = forms.TimeField(required=True, help_text='в формате "ЧЧ:ММ"')

    class Meta:
        model = Reception
        exclude = ('date_create',)