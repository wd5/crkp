# -*- coding: utf-8 -*-
from django.db.models import Max
from apps.services.models import Service
from apps.servicerequests.forms import TypicalRequestForm, FirstServRequestForm, ReceptionForm, SecondServRequestForm
from apps.servicerequests.models import FirstServRequest, SecondServRequest
from django.views.generic import  DetailView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template.loader import render_to_string
from apps.utils.utils import render_to_pdf
import settings

class ReqFormLoaderView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse()
        id = self.kwargs.get('id', None)
        try:
            id = int(id)
        except ValueError:
            return HttpResponseBadRequest()
        try:
            service_curr = Service.objects.get(pk=id)
            service_title = service_curr.title
        except Service.DoesNotExist:
            return HttpResponseBadRequest()

        if id in [1, 2, 3, 4, 5]:
            if id == 1:
                form = FirstServRequestForm()
                case = 'first_serv'
            elif id == 2:
                form = SecondServRequestForm()
                case = 'second_serv'
            else:
                form = False
                case = False
        elif id == 10:
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
                {'form': form, 'case': case, 'service_title': service_title}
        )
        response.content = items_html
        return response

load_request_form = ReqFormLoaderView.as_view()

class ReqFormCheckView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = request.POST.copy()
            if 'form_type' not in request.POST:
                return HttpResponseBadRequest()
            else:
                form_type = request.POST['form_type']
                if form_type == 'typical':
                    form = TypicalRequestForm(data)
                    if form.is_valid():
                        form.save()
                        return HttpResponse('success')
                    else:
                        id = request.POST['service']
                        try:
                            id = int(id)
                        except ValueError:
                            return HttpResponseBadRequest()
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
                        saved_object = form.save()
                        path = render_to_pdf('services/pdf.html', 'first_serv_%s' % saved_object.pk, {
                            'title': u'Заявка на договор и технические условия на подключение к электрическим сетям, физические лица до 15 кВт (включительно)',
                            'saved_object': saved_object,
                            'case': request.POST['form_type'],
                            'MEDIA_ROOT': settings.ROOT_PATH
                        })
                        saved_object.generated_pdf = 'uploads/files/guests/guest_first_serv_%s.pdf' % saved_object.pk
                        saved_object.save()

                        RecForm = ReceptionForm()
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': RecForm, 'case': 'reception_form', 'pdf_path': saved_object.generated_pdf,
                                 'id_serv': saved_object.pk, 'serv_type': 'first_serv'}
                        )
                        return HttpResponse(items_html)
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], }
                        )
                        return HttpResponse(items_html)
                elif form_type == 'second_serv':
                    form = SecondServRequestForm(data)
                    if form.is_valid():
                        saved_object = form.save()
                        path = render_to_pdf('services/pdf.html', 'second_serv_%s' % saved_object.pk, {
                            'title': u'Заявка на договор и технические условия на подключение к электрическим сетям, физические лица до 100 кВт (включительно)',
                            'saved_object': saved_object,
                            'case': request.POST['form_type'],
                            'MEDIA_ROOT': settings.ROOT_PATH
                        })
                        saved_object.generated_pdf = 'uploads/files/guests/guest_second_serv_%s.pdf' % saved_object.pk
                        saved_object.save()

                        RecForm = ReceptionForm()
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
                elif form_type == 'reception_form':
                    form = ReceptionForm(data)
                    if form.is_valid():
                        saved_object = form.save()
                        try:
                            id_serv = int(request.POST['id_serv'])
                        except:
                            return HttpResponseBadRequest()

                        if request.POST['serv_type'] == 'first_serv':
                            try:
                                related_serv = FirstServRequest.objects.get(pk=id_serv)
                            except FirstServRequest.DoesNotExist:
                                return HttpResponseBadRequest()

                        if request.POST['serv_type'] == 'second_serv':
                            try:
                                related_serv = SecondServRequest.objects.get(pk=id_serv)
                            except SecondServRequest.DoesNotExist:
                                return HttpResponseBadRequest()

                        related_serv.connection_request = saved_object
                        related_serv.save()
                        return HttpResponse('success')
                    else:
                        items_html = render_to_string(
                            'services/form_load_template.html',
                                {'form': form, 'case': request.POST['form_type'], 'pdf_path': request.POST['pdf_path'],
                                 'id_serv': request.POST['id_serv'], 'serv_type':request.POST['serv_type']}
                        )
                        return HttpResponse(items_html)
        else:
            return HttpResponseBadRequest()

check_request_form = ReqFormCheckView.as_view()