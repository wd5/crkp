# -*- coding: utf-8 -*-
from apps.pages.models import Page
from apps.techconnection.models import MapPolygon,Electroload
from apps.pages.views import ShowCompItemView
from django.views.generic import ListView,DetailView,TemplateView

class ShowTechItemView(ShowCompItemView):
    template_name = 'techconnection/tech_blocks.html'

show_tech_item = ShowTechItemView.as_view()

class ShowRatesMapView(ListView):
    model = MapPolygon
    template_name = 'techconnection/map_rates.html'
    context_object_name = 'polygons'

    def get_context_data(self, **kwargs):
        context = super(ShowRatesMapView,self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(pk=11)
        return context

show_rates_map = ShowRatesMapView.as_view()

class ShowRatesTableView(DetailView):
    slug_field = 'number'
    model = MapPolygon
    template_name = 'techconnection/map_modal.html'
    context_object_name = 'polygon'

show_rates_table = ShowRatesTableView.as_view()

class ShowTechCalcView(ListView):
    model = Electroload
    template_name = 'techconnection/tech_calc.html'
    context_object_name = 'electroloads'
    queryset = model.objects.published()

    def get_context_data(self, **kwargs):
        context = super(ShowTechCalcView,self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(pk=14)
        counter = 0
        parameters = ''
        for item in self.object_list:
            counter = counter + 1
            parameters = u'%s,%s,%s|' % (parameters, item.id,0)
        if parameters.startswith(',') or parameters.startswith('|'):
            parameters = parameters[1:]
            if parameters.endswith(',') or parameters.endswith('|'):
                parameters = parameters[:-1]
            parameters = parameters.replace('|,', '|')
        context['parameters'] = parameters
        return context

show_techcalc = ShowTechCalcView.as_view()