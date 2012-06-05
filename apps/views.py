# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from apps.siteblocks.models import Settings

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['maintxt_first'] = Settings.objects.get(name="main_first")
        context['maintxt_second'] = Settings.objects.get(name="main_second")
        return context

index = IndexView.as_view()