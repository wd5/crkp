# -*- coding: utf-8 -*-
from apps.services.models import Service
from apps.servicerequests.forms import TypicalRequestForm #,FirstServRequestForm
from django.views.generic import  DetailView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template.loader import render_to_string

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
#                service_set = Service.objects.filter(pk=id)
#                form = FirstServRequestForm()
#                form.fields['service'].queryset = service_set
#                form.initial['service'] = service_curr
                form = False
                case = 'first_serv'
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
        else:
            return HttpResponseBadRequest()

check_request_form = ReqFormCheckView.as_view()