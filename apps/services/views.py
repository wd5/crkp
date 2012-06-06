# -*- coding: utf-8 -*-
from AptUrl.Helpers import _
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from apps.services.models import Service
from apps.services.forms import TypicalRequestForm
from django.views.generic import ListView, DetailView, TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.template.loader import render_to_string


class ShowServiceView(DetailView):
    model = Service
    template_name = 'services/show_service.html'
    context_object_name = 'service'

    def get(self, request, **kwargs):
        self.object = self.get_object()
        if self.object.id in [2,3,4,5]:
            return HttpResponseRedirect(reverse('show_service'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

show_service = ShowServiceView.as_view()

class ServLoaderView(View):
    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseRedirect('/')
        else:
            if 'id' not in request.POST:
                return HttpResponseBadRequest()

        id = request.POST['id']
        try:
            id = int(id)
        except ValueError:
            return HttpResponseBadRequest()

        try:
            service = Service.objects.get(pk=id)
        except Service.DoesNotExist:
            return HttpResponseBadRequest()

        response = HttpResponse()
        items_html = render_to_string(
            'services/serv_load_template.html',
                {'service': service}
        )
        response.content = items_html
        return response

load_serv = ServLoaderView.as_view()

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
            service_title = False

        if id in [1, 2, 3, 4, 5]:
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