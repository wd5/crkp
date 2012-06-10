# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from apps.services.models import Service
from django.views.generic import  DetailView, View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
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