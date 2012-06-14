# -*- coding: utf-8 -*-
from django import forms
from apps.servicerequests.models import TypicalRequest, FirstServRequest, Reception, SecondServRequest, ThirdServRequest, FourthServRequest, FifthServRequest

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

    agent_full_name = forms.CharField(required=True)
    authority_number = forms.CharField(required=True)
    authority_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    phone_number = forms.CharField(required=True)
    fax = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    req_attachment1 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment1')[0].verbose_name)
    req_attachment2 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment2')[0].verbose_name)
    req_attachment3 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment3')[0].verbose_name)
    req_attachment4 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment4')[0].verbose_name)
    req_attachment5 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment5')[0].verbose_name)
    req_attachment6 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment6')[0].verbose_name)
    req_attachment7 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment7')[0].verbose_name)
    req_attachment8 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment8')[0].verbose_name)
    req_attachment9 = forms.BooleanField(required=False, label=FirstServRequest._meta.get_field_by_name('req_attachment9')[0].verbose_name)

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

    load_type = forms.CharField(required=True)
    other_inf = forms.CharField(widget=forms.Textarea, required=True)

    agent_full_name = forms.CharField(required=True)
    authority_number = forms.CharField(required=True)
    authority_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    phone_number = forms.CharField(required=True)
    fax = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    req_attachment1 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment1')[0].verbose_name)
    req_attachment2 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment2')[0].verbose_name)
    req_attachment3 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment3')[0].verbose_name)
    req_attachment4 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment4')[0].verbose_name)
    req_attachment5 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment5')[0].verbose_name)
    req_attachment6 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment6')[0].verbose_name)
    req_attachment7 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment7')[0].verbose_name)
    req_attachment8 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment8')[0].verbose_name)
    req_attachment9 = forms.BooleanField(required=False, label=SecondServRequest._meta.get_field_by_name('req_attachment9')[0].verbose_name)

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

class ThirdServRequestForm(forms.ModelForm):
    org_title = forms.CharField(widget=forms.Textarea, required=True)
    egrul_number = forms.CharField(widget=forms.Textarea, required=True)
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

    agent_full_name = forms.CharField(required=True)
    authority_number = forms.CharField(required=True)
    authority_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    phone_number = forms.CharField(required=True)
    fax = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    director_post = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('director_post')[0].verbose_name)
    director_full_name = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('director_full_name')[0].verbose_name)

    agent_inn = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('agent_inn')[0].verbose_name)
    agent_kpp = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('agent_kpp')[0].verbose_name)
    agent_bik = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('agent_bik')[0].verbose_name)
    agent_bank_title = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('agent_bank_title')[0].verbose_name)
    agent_bank_account = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('agent_bank_account')[0].verbose_name)
    agent_correspond_account = forms.CharField(required=True, label=ThirdServRequest._meta.get_field_by_name('agent_correspond_account')[0].verbose_name)

    req_attachment1 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment1')[0].verbose_name)
    req_attachment2 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment2')[0].verbose_name)
    req_attachment3 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment3')[0].verbose_name)
    req_attachment4 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment4')[0].verbose_name)
    req_attachment5 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment5')[0].verbose_name)
    req_attachment6 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment6')[0].verbose_name)
    req_attachment7 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment7')[0].verbose_name)
    req_attachment8 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment8')[0].verbose_name)
    req_attachment9 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment9')[0].verbose_name)
    req_attachment10 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment10')[0].verbose_name)
    req_attachment11 = forms.BooleanField(required=False, label=ThirdServRequest._meta.get_field_by_name('req_attachment11')[0].verbose_name)

    class Meta:
        model = ThirdServRequest
        exclude = ('connection_request', 'generated_pdf', 'date_create',)

    def clean_agent_inn(self):
        agent_inn = self.cleaned_data['agent_inn']
        try:
            integer = int(agent_inn)
        except:
            integer = False

        if (len(agent_inn) != 10 and len(agent_inn) != 12) or not integer:
            raise forms.ValidationError("ИНН содержит 10 или 12 цифр (сейчас %s)"%len(agent_inn))
        return agent_inn

    def clean_agent_kpp(self):
        agent_kpp = self.cleaned_data['agent_kpp']
        try:
            integer = int(agent_kpp)
        except:
            integer = False

        if len(agent_kpp) != 9 or not integer:
            raise forms.ValidationError("КПП содержит 9 цифр (сейчас %s)"%len(agent_kpp))
        return agent_kpp

    def clean_agent_bik(self):
        agent_bik = self.cleaned_data['agent_bik']
        try:
            integer = int(agent_bik)
        except:
            integer = False

        if len(agent_bik) != 9 or not integer:
            raise forms.ValidationError("БИК содержит 9 цифр (сейчас %s)"%len(agent_bik))
        return agent_bik

    def clean_agent_bank_account(self):
        agent_bank_account = self.cleaned_data['agent_bank_account']
        try:
            integer = int(agent_bank_account)
        except:
            integer = False

        if len(agent_bank_account) != 20 or not integer:
            raise forms.ValidationError("Расчетный счёт содержит 20 цифр (сейчас %s)"%len(agent_bank_account))
        return agent_bank_account

    def clean_agent_correspond_account(self):
        agent_correspond_account = self.cleaned_data['agent_correspond_account']
        try:
            integer = int(agent_correspond_account)
        except:
            integer = False

        if len(agent_correspond_account) != 20 or not integer:
            raise forms.ValidationError("Корреспондентский счет содержит 20 цифр (сейчас %s)"%len(agent_correspond_account))
        return agent_correspond_account

class FourthServRequestForm(forms.ModelForm):
    org_title = forms.CharField(widget=forms.Textarea, required=True)
    egrul_number = forms.CharField(widget=forms.Textarea, required=True)
    egrul_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')

    actual_address_with_index = forms.CharField(widget=forms.Textarea, required=True)
    object_title = forms.CharField(required=True)
    object_location = forms.CharField(widget=forms.Textarea, required=True)

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

    count_conn_points = forms.CharField(widget=forms.Textarea, required=True)
    load_type = forms.CharField(widget=forms.Textarea, required=True)
    power_distribution = forms.CharField(widget=forms.Textarea, required=True)
    other_inf = forms.CharField(widget=forms.Textarea, required=True)

    agent_full_name = forms.CharField(required=True)
    authority_number = forms.CharField(required=True)
    authority_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    phone_number = forms.CharField(required=True)
    fax = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    director_post = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('director_post')[0].verbose_name)
    director_full_name = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('director_full_name')[0].verbose_name)

    agent_inn = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('agent_inn')[0].verbose_name)
    agent_kpp = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('agent_kpp')[0].verbose_name)
    agent_bik = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('agent_bik')[0].verbose_name)
    agent_bank_title = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('agent_bank_title')[0].verbose_name)
    agent_bank_account = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('agent_bank_account')[0].verbose_name)
    agent_correspond_account = forms.CharField(required=True, label=FourthServRequest._meta.get_field_by_name('agent_correspond_account')[0].verbose_name)

    req_attachment1 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment1')[0].verbose_name)
    req_attachment2 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment2')[0].verbose_name)
    req_attachment3 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment3')[0].verbose_name)
    req_attachment4 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment4')[0].verbose_name)
    req_attachment5 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment5')[0].verbose_name)
    req_attachment6 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment6')[0].verbose_name)
    req_attachment7 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment7')[0].verbose_name)
    req_attachment8 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment8')[0].verbose_name)
    req_attachment9 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment9')[0].verbose_name)
    req_attachment10 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment10')[0].verbose_name)
    req_attachment11 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment11')[0].verbose_name)
    req_attachment12 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment12')[0].verbose_name)
    req_attachment13 = forms.BooleanField(required=False, label=FourthServRequest._meta.get_field_by_name('req_attachment13')[0].verbose_name)

    class Meta:
        model = FourthServRequest
        exclude = ('connection_request', 'generated_pdf', 'date_create',)

    def clean_agent_inn(self):
        agent_inn = self.cleaned_data['agent_inn']
        try:
            integer = int(agent_inn)
        except:
            integer = False

        if (len(agent_inn) != 10 and len(agent_inn) != 12) or not integer:
            raise forms.ValidationError("ИНН содержит 10 или 12 цифр (сейчас %s)"%len(agent_inn))
        return agent_inn

    def clean_agent_kpp(self):
        agent_kpp = self.cleaned_data['agent_kpp']
        try:
            integer = int(agent_kpp)
        except:
            integer = False

        if len(agent_kpp) != 9 or not integer:
            raise forms.ValidationError("КПП содержит 9 цифр (сейчас %s)"%len(agent_kpp))
        return agent_kpp

    def clean_agent_bik(self):
        agent_bik = self.cleaned_data['agent_bik']
        try:
            integer = int(agent_bik)
        except:
            integer = False

        if len(agent_bik) != 9 or not integer:
            raise forms.ValidationError("БИК содержит 9 цифр (сейчас %s)"%len(agent_bik))
        return agent_bik

    def clean_agent_bank_account(self):
        agent_bank_account = self.cleaned_data['agent_bank_account']
        try:
            integer = int(agent_bank_account)
        except:
            integer = False

        if len(agent_bank_account) != 20 or not integer:
            raise forms.ValidationError("Расчетный счёт содержит 20 цифр (сейчас %s)"%len(agent_bank_account))
        return agent_bank_account

    def clean_agent_correspond_account(self):
        agent_correspond_account = self.cleaned_data['agent_correspond_account']
        try:
            integer = int(agent_correspond_account)
        except:
            integer = False

        if len(agent_correspond_account) != 20 or not integer:
            raise forms.ValidationError("Корреспондентский счет содержит 20 цифр (сейчас %s)"%len(agent_correspond_account))
        return agent_correspond_account

class FifthServRequestForm(forms.ModelForm):
    org_title = forms.CharField(widget=forms.Textarea, required=True)
    egrul_number = forms.CharField(widget=forms.Textarea, required=True)
    egrul_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')

    actual_address_with_index = forms.CharField(widget=forms.Textarea, required=True)
    object_title = forms.CharField(required=True)
    object_location = forms.CharField(widget=forms.Textarea, required=True)

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

    cnt_pwr_transformers = forms.CharField(widget=forms.Textarea, required=True)
    cnt_pwr_generators = forms.CharField(widget=forms.Textarea, required=True)

    count_conn_points = forms.CharField(widget=forms.Textarea, required=True)
    load_type = forms.CharField(widget=forms.Textarea, required=True)

    tech_min_generators = forms.CharField(widget=forms.Textarea, required=True)
    tech_armor_consumer = forms.CharField(widget=forms.Textarea, required=True)
    tech_emergency_armor_consumer = forms.CharField(widget=forms.Textarea, required=True)

    power_distribution = forms.CharField(widget=forms.Textarea, required=True)
    other_inf = forms.CharField(widget=forms.Textarea, required=True)

    agent_full_name = forms.CharField(required=True)
    authority_number = forms.CharField(required=True)
    authority_date = forms.DateField(widget=forms.DateInput, required=True, help_text='в формате "ДД.ММ.ГГГГ"')
    phone_number = forms.CharField(required=True)
    fax = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    director_post = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('director_post')[0].verbose_name)
    director_full_name = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('director_full_name')[0].verbose_name)

    agent_inn = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('agent_inn')[0].verbose_name)
    agent_kpp = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('agent_kpp')[0].verbose_name)
    agent_bik = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('agent_bik')[0].verbose_name)
    agent_bank_title = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('agent_bank_title')[0].verbose_name)
    agent_bank_account = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('agent_bank_account')[0].verbose_name)
    agent_correspond_account = forms.CharField(required=True, label=FifthServRequest._meta.get_field_by_name('agent_correspond_account')[0].verbose_name)

    req_attachment1 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment1')[0].verbose_name)
    req_attachment2 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment2')[0].verbose_name)
    req_attachment3 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment3')[0].verbose_name)
    req_attachment4 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment4')[0].verbose_name)
    req_attachment5 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment5')[0].verbose_name)
    req_attachment6 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment6')[0].verbose_name)
    req_attachment7 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment7')[0].verbose_name)
    req_attachment8 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment8')[0].verbose_name)
    req_attachment9 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment9')[0].verbose_name)
    req_attachment10 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment10')[0].verbose_name)
    req_attachment11 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment11')[0].verbose_name)
    req_attachment12 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment12')[0].verbose_name)
    req_attachment13 = forms.BooleanField(required=False, label=FifthServRequest._meta.get_field_by_name('req_attachment13')[0].verbose_name)

    class Meta:
        model = FifthServRequest
        exclude = ('connection_request', 'generated_pdf', 'date_create',)

    def clean_agent_inn(self):
        agent_inn = self.cleaned_data['agent_inn']
        try:
            integer = int(agent_inn)
        except:
            integer = False

        if (len(agent_inn) != 10 and len(agent_inn) != 12) or not integer:
            raise forms.ValidationError("ИНН содержит 10 или 12 цифр (сейчас %s)"%len(agent_inn))
        return agent_inn

    def clean_agent_kpp(self):
        agent_kpp = self.cleaned_data['agent_kpp']
        try:
            integer = int(agent_kpp)
        except:
            integer = False

        if len(agent_kpp) != 9 or not integer:
            raise forms.ValidationError("КПП содержит 9 цифр (сейчас %s)"%len(agent_kpp))
        return agent_kpp

    def clean_agent_bik(self):
        agent_bik = self.cleaned_data['agent_bik']
        try:
            integer = int(agent_bik)
        except:
            integer = False

        if len(agent_bik) != 9 or not integer:
            raise forms.ValidationError("БИК содержит 9 цифр (сейчас %s)"%len(agent_bik))
        return agent_bik

    def clean_agent_bank_account(self):
        agent_bank_account = self.cleaned_data['agent_bank_account']
        try:
            integer = int(agent_bank_account)
        except:
            integer = False

        if len(agent_bank_account) != 20 or not integer:
            raise forms.ValidationError("Расчетный счёт содержит 20 цифр (сейчас %s)"%len(agent_bank_account))
        return agent_bank_account

    def clean_agent_correspond_account(self):
        agent_correspond_account = self.cleaned_data['agent_correspond_account']
        try:
            integer = int(agent_correspond_account)
        except:
            integer = False

        if len(agent_correspond_account) != 20 or not integer:
            raise forms.ValidationError("Корреспондентский счет содержит 20 цифр (сейчас %s)"%len(agent_correspond_account))
        return agent_correspond_account

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