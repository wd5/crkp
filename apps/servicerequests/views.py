# -*- coding: utf-8 -*-
from django.db.models import Max
from apps.services.models import Service
from apps.servicerequests.forms import TypicalRequestForm, FirstServRequestForm, ReceptionForm, SecondServRequestForm, ThirdServRequestForm, FourthServRequestForm, FifthServRequestForm
from apps.servicerequests.models import FirstServRequest, SecondServRequest, ThirdServRequest, FourthServRequest, FifthServRequest, BlackList
from apps.siteblocks.models import Settings
from django.views.generic import  DetailView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template.loader import render_to_string
from apps.utils.utils import render_to_pdf
from django.core.mail.message import EmailMessage
import settings

class ReqFormLoaderView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse()
        id = self.kwargs.get('id', None)
        try:
            id = int(id)
        except ValueError:
            return HttpResponseBadRequest(
                "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
        try:
            service_curr = Service.objects.get(pk=id)
            service_title = service_curr.title
        except Service.DoesNotExist:
            return HttpResponseBadRequest(
                "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

        if id in [1, 2, 3, 4, 5]:
            if id == 1:
                form = FirstServRequestForm()
                case = 'first_serv'
            elif id == 2:
                form = SecondServRequestForm()
                case = 'second_serv'
            elif id == 3:
                form = ThirdServRequestForm()
                case = 'third_serv'
            elif id == 4:
                form = FourthServRequestForm()
                case = 'fourth_serv'
            elif id == 5:
                form = FifthServRequestForm()
                case = 'fifth_serv'
            else:
                form = False
                case = False
        else:
            service_set = Service.objects.filter(pk=id)
            form = TypicalRequestForm()
            form.fields['service'].queryset = service_set
            form.initial['service'] = service_curr
            case = 'typical'

        items_html = render_to_string(
            'services/form_load_template.html',
                {'form': form, 'case': case, 'service_title': service_title, }
        )
        response.content = items_html
        return response

load_request_form = ReqFormLoaderView.as_view()

def CheckRequest(full_name, phonenum, email):
    full_name = full_name.strip()
    phonenum = phonenum.strip()
    email = email.strip()
    if full_name == '' or phonenum == '' or email == '':
        return True
    else:
        black_list = BlackList.objects.all()
        full_name = full_name.split(' ')
        f = full_name[0]
        try:
            i = full_name[1]
        except:
            i = False
        if i:
            try:
                o = full_name[2]
            except:
                o = False
        else:
            o = False

        if f and i and o:
            f_fio = black_list.filter(full_name__icontains=f).filter(full_name__icontains=i).filter(full_name__icontains=o)
        elif f and i:
            f_fio = black_list.filter(full_name__icontains=f).filter(full_name__icontains=i)
        elif f:
            f_fio = black_list.filter(full_name__icontains=f)
        else:
            f_fio = False

        f_phone = black_list.filter(phonenumber__iexact='%s' % phonenum)
        f_email = black_list.filter(email__iexact='%s' % email)
        if f_fio or f_phone or f_email:
            result = True
        else:
            result = False
        return result

class ReqFormCheckView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = request.POST.copy()
            if 'form_type' not in request.POST:
                return HttpResponseBadRequest(
                    "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
            else:
                form_type = request.POST['form_type']
                if form_type == 'typical':
                    form = TypicalRequestForm(data)
                    if form.is_valid():

                        if form.cleaned_data['email']=='':
                            email = '-'
                        else:
                            email = form.cleaned_data['email']

                        if form.cleaned_data['phonenumber']=='':
                            phonenumber = '-'
                        else:
                            phonenumber = form.cleaned_data['phonenumber']

                        # проверка по черному списку:
                        check_result = CheckRequest(form.cleaned_data['full_name'], phonenumber, email)
                        if check_result:
                            return HttpResponseBadRequest(
                                "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
                        else:
                            saved_object = form.save()

                            subject = u'ООО ЦРКП - Информация о добавлении заявки.'
                            subject = u''.join(subject.splitlines())
                            message = render_to_string(
                                'services/message_template_2.html',
                                    {
                                    'saved_object': saved_object,
                                    }
                            )
                            try:
                                emailto = Settings.objects.get(name='workemail').value
                            except Settings.DoesNotExist:
                                emailto = False

                            if emailto:
                                msg = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [emailto])
                                msg.content_subtype = "html"
                                msg.send()
                            return HttpResponse('success')
                    else:
                        id = request.POST['service']
                        try:
                            id = int(id)
                        except ValueError:
                            return HttpResponseBadRequest(
                                "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
                        service_set = Service.objects.filter(pk=id)
                        form.fields['service'].queryset = service_set
                        service_title = Service.objects.get(pk=id).title
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], 'service_title': service_title}
                        )
                        return HttpResponse(items_html)
                elif form_type == 'first_serv':
                    form = FirstServRequestForm(data)
                    if form.is_valid():

                        if form.cleaned_data['email']=='':
                            email = '-'
                        else:
                            email = form.cleaned_data['email']
                        # проверка по черному списку:
                        check_result = CheckRequest('%s %s %s' % (form.cleaned_data['agent_last_name'],form.cleaned_data['agent_first_name'],form.cleaned_data['agent_middle_name']), form.cleaned_data['phone_number'], email)

#                        if check_result:
#                            return HttpResponseBadRequest("<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
#                        else:

                        saved_object = form.save()

                        path = render_to_pdf('services/pdf.html', 'first_serv_%s' % saved_object.pk, {
                            'title': u'Физические лица до 15 кВт (включительно) по 3 категории надежности электроснабжения',
                            'saved_object': saved_object,
                            'case': request.POST['form_type'],
                            'MEDIA_ROOT': settings.ROOT_PATH
                        })
                        saved_object.generated_pdf = 'uploads/files/guests/guest_first_serv_%s.pdf' % saved_object.pk
                        saved_object.save()

                        RecForm = ReceptionForm()

                        if check_result:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,}
                            )
                            saved_object.delete()
                        else:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'form': RecForm, 'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,
                                     'id_serv': saved_object.pk, 'serv_type': 'first_serv',}
                            )
                        return HttpResponse(items_html)
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'],}
                        )
                        return HttpResponse(items_html)
                elif form_type == 'second_serv':
                    form = SecondServRequestForm(data)
                    if form.is_valid():

                        if form.cleaned_data['email']=='':
                            email = '-'
                        else:
                            email = form.cleaned_data['email']
                        # проверка по черному списку:
                        check_result = CheckRequest('%s %s %s' % (form.cleaned_data['agent_last_name'],form.cleaned_data['agent_first_name'],form.cleaned_data['agent_middle_name']), form.cleaned_data['phone_number'], email)
#                        if check_result:
#                            return HttpResponseBadRequest("<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
#                        else:
                        saved_object = form.save()

                        path = render_to_pdf('services/pdf.html', 'second_serv_%s' % saved_object.pk, {
                            'title': u'Физические лица до 100 кВт (включительно) по 1,2,3 категории надежности электроснабжения ВРЕМЕННОЕ присоединение',
                            'saved_object': saved_object,
                            'case': request.POST['form_type'],
                            'MEDIA_ROOT': settings.ROOT_PATH
                        })
                        saved_object.generated_pdf = 'uploads/files/guests/guest_second_serv_%s.pdf' % saved_object.pk
                        saved_object.save()

                        RecForm = ReceptionForm()

                        if check_result:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,}
                            )
                            saved_object.delete()
                        else:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'form': RecForm, 'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,
                                     'id_serv': saved_object.pk, 'serv_type': 'second_serv'}
                            )
                        return HttpResponse(items_html)
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], }
                        )
                        return HttpResponse(items_html)
                elif form_type == 'third_serv':
                    form = ThirdServRequestForm(data)
                    if form.is_valid():

                        if form.cleaned_data['email']=='':
                            email = '-'
                        else:
                            email = form.cleaned_data['email']
                        # проверка по черному списку:
                        check_result = CheckRequest('%s %s %s' % (form.cleaned_data['agent_last_name'],form.cleaned_data['agent_first_name'],form.cleaned_data['agent_middle_name']), form.cleaned_data['phone_number'], email)
#                        if check_result:
#                            return HttpResponseBadRequest("<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
#                        else:
                        saved_object = form.save()

                        path = render_to_pdf('services/pdf.html', 'third_serv_%s' % saved_object.pk, {
                            'title': u'Юридические лица и индивидуальные предприниматели до 100 кВт (включительно) по 1, 2, 3 категории надежности электроснабжения ВРЕМЕННОЕ присоединение',
                            'saved_object': saved_object,
                            'case': request.POST['form_type'],
                            'MEDIA_ROOT': settings.ROOT_PATH
                        })
                        saved_object.generated_pdf = 'uploads/files/guests/guest_third_serv_%s.pdf' % saved_object.pk
                        saved_object.save()

                        RecForm = ReceptionForm()

                        if check_result:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,}
                            )
                            saved_object.delete()
                        else:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'form': RecForm, 'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,
                                     'id_serv': saved_object.pk, 'serv_type': 'third_serv'}
                            )
                        return HttpResponse(items_html)
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], }
                        )
                        return HttpResponse(items_html)
                elif form_type == 'fourth_serv':
                    form = FourthServRequestForm(data)
                    if form.is_valid():

                        if form.cleaned_data['email']=='':
                            email = '-'
                        else:
                            email = form.cleaned_data['email']
                        # проверка по черному списку:
                        check_result = CheckRequest('%s %s %s' % (form.cleaned_data['agent_last_name'],form.cleaned_data['agent_first_name'],form.cleaned_data['agent_middle_name']), form.cleaned_data['phone_number'], email)
#                        if check_result:
#                            return HttpResponseBadRequest("<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
#                        else:
                        saved_object = form.save()

                        path = render_to_pdf('services/pdf.html', 'fourth_serv_%s' % saved_object.pk, {
                            'title': u'Юридические лица и индивидуальные предприниматели до 750 кВА (включительно) по 1, 2, 3 категории надежности электроснабжения',
                            'saved_object': saved_object,
                            'case': request.POST['form_type'],
                            'MEDIA_ROOT': settings.ROOT_PATH
                        })
                        saved_object.generated_pdf = 'uploads/files/guests/guest_fourth_serv_%s.pdf' % saved_object.pk
                        saved_object.save()

                        RecForm = ReceptionForm()

                        if check_result:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,}
                            )
                            saved_object.delete()
                        else:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'form': RecForm, 'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,
                                     'id_serv': saved_object.pk, 'serv_type': 'fourth_serv'}
                            )
                        return HttpResponse(items_html)
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], }
                        )
                        return HttpResponse(items_html)
                elif form_type == 'fifth_serv':
                    form = FifthServRequestForm(data)
                    if form.is_valid():

                        if form.cleaned_data['email']=='':
                            email = '-'
                        else:
                            email = form.cleaned_data['email']
                        # проверка по черному списку:
                        check_result = CheckRequest('%s %s %s' % (form.cleaned_data['agent_last_name'],form.cleaned_data['agent_first_name'],form.cleaned_data['agent_middle_name']), form.cleaned_data['phone_number'], email)
#                        if check_result:
#                            return HttpResponseBadRequest("<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")
#                        else:
                        saved_object = form.save()

                        path = render_to_pdf('services/pdf.html', 'fifth_serv_%s' % saved_object.pk, {
                            'title': u'Юридические лица и индивидуальные предприниматели свыше 750 кВА по 1,2,3 категории надежности электроснабжения',
                            'saved_object': saved_object,
                            'case': request.POST['form_type'],
                            'MEDIA_ROOT': settings.ROOT_PATH
                        })
                        saved_object.generated_pdf = 'uploads/files/guests/guest_fifth_serv_%s.pdf' % saved_object.pk
                        saved_object.save()

                        RecForm = ReceptionForm()

                        if check_result:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,}
                            )
                            saved_object.delete()
                        else:
                            items_html = render_to_string(
                                'services/form_load_template.html',
                                    {'form': RecForm, 'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,
                                     'id_serv': saved_object.pk, 'serv_type': 'fifth_serv'}
                            )
                        return HttpResponse(items_html)
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], }
                        )
                        return HttpResponse(items_html)
                elif form_type == 'reception_form':
                    form = ReceptionForm(data)
                    if form.is_valid():
                        saved_object = form.save()
                        try:
                            id_serv = int(request.POST['id_serv'])
                        except:
                            return HttpResponseBadRequest(
                                "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

                        if request.POST['serv_type'] == 'first_serv':
                            try:
                                serv_type=u'Физические лица до 15 кВт (включительно) по 3 категории надежности электроснабжения'
                                related_serv = FirstServRequest.objects.get(pk=id_serv)
                            except FirstServRequest.DoesNotExist:
                                return HttpResponseBadRequest(
                                    "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

                        if request.POST['serv_type'] == 'second_serv':
                            try:
                                serv_type=u'Физические лица до 100 кВт (включительно) по 1,2,3 категории надежности электроснабжения ВРЕМЕННОЕ присоединение'
                                related_serv = SecondServRequest.objects.get(pk=id_serv)
                            except SecondServRequest.DoesNotExist:
                                return HttpResponseBadRequest(
                                    "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

                        if request.POST['serv_type'] == 'third_serv':
                            try:
                                serv_type=u'Юридические лица и индивидуальные предприниматели до 100 кВт (включительно) по 1, 2, 3 категории надежности электроснабжения ВРЕМЕННОЕ присоединение'
                                related_serv = ThirdServRequest.objects.get(pk=id_serv)
                            except ThirdServRequest.DoesNotExist:
                                return HttpResponseBadRequest(
                                    "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

                        if request.POST['serv_type'] == 'fourth_serv':
                            try:
                                serv_type=u'Юридические лица и индивидуальные предприниматели до 750 кВА (включительно) по 1, 2, 3 категории надежности электроснабжения'
                                related_serv = FourthServRequest.objects.get(pk=id_serv)
                            except FourthServRequest.DoesNotExist:
                                return HttpResponseBadRequest(
                                    "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

                        if request.POST['serv_type'] == 'fifth_serv':
                            try:
                                serv_type=u'Юридические лица и индивидуальные предприниматели свыше 750 кВА по 1,2,3 категории надежности электроснабжения'
                                related_serv = FifthServRequest.objects.get(pk=id_serv)
                            except FifthServRequest.DoesNotExist:
                                return HttpResponseBadRequest(
                                    "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

                        related_serv.connection_request = saved_object
                        related_serv.save()

                        subject = u'ООО ЦРКП - Информация о записи на приём.'
                        subject = u''.join(subject.splitlines())
                        message = render_to_string(
                            'services/message_template.html',
                                {
                                'saved_object': saved_object,'serv_type':serv_type,
                                }
                        )
                        try:
                            emailto = Settings.objects.get(name='workemail').value
                        except Settings.DoesNotExist:
                            emailto = False

                        if emailto:
                            msg = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [emailto])
                            msg.content_subtype = "html"
                            msg.send()

                        return HttpResponse('success')
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], 'pdf_path': request.POST['pdf_path'],
                                 'id_serv': request.POST['id_serv'], 'serv_type': request.POST['serv_type']}
                        )
                        return HttpResponse(items_html)
        else:
            return HttpResponseBadRequest(
                "<div style='height: 150px;text-align: center;padding-top: 75px;'>Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.</div>")

check_request_form = ReqFormCheckView.as_view()