# -*- coding: utf-8 -*-
from django.http import HttpResponseBadRequest, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from apps.pages.models import Page
from apps.techconnection.models import MapPolygon, Electroload
from apps.pages.views import ShowCompItemView
from django.views.generic import ListView, DetailView, TemplateView, View
from decimal import Decimal

class ShowTechItemView(ShowCompItemView):
    template_name = 'techconnection/tech_blocks.html'

show_tech_item = ShowTechItemView.as_view()

class ShowRatesMapView(ListView):
    model = MapPolygon
    template_name = 'techconnection/map_rates.html'
    context_object_name = 'polygons'

    def get_context_data(self, **kwargs):
        context = super(ShowRatesMapView, self).get_context_data(**kwargs)
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
        context = super(ShowTechCalcView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(pk=14)
        parameters = ''
        for item in self.object_list:
            parameters = u'%s,%s,%s|' % (parameters, item.id, 0)
        if parameters.startswith(',') or parameters.startswith('|'):
            parameters = parameters[1:]
            if parameters.endswith(',') or parameters.endswith('|'):
                parameters = parameters[:-1]
            parameters = parameters.replace('|,', '|')
        context['parameters'] = parameters
        return context

show_techcalc = ShowTechCalcView.as_view()

class CalculateView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if 'parameters' not in request.POST:
                return HttpResponseBadRequest(
                    "Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.")
            parameters = request.POST['parameters']
            parameters_array = parameters.split('|')
            Ppo = 0
            Ppb = 0
            Ppc1 = 0
            Ppc2 = 0
            Ppc3 = 0
            Ppc4 = 0
            PpcAdded = 0
            if len(parameters_array) != 0:
                for parameter in parameters_array:
                    parts = parameter.split(',')
                    if parts[0] != 'added':
                        try:
                            id_el = int(parts[0])
                            count_el = int(parts[1])
                        except ValueError:
                            return HttpResponseBadRequest(
                                "Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.")
                        try:
                            electoload = Electroload.objects.get(id=id_el)
                        except Electroload.DoesNotExist:
                            return HttpResponseBadRequest(
                                "Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.")
                        power = electoload.power_parameter
                        el_parameters = electoload.get_parameters()
                        parameter_demand = 0
                        if count_el!=0:
                            for el_parameter in el_parameters:
                                if parameter_demand == 0:
                                    if el_parameter.count_type == 'single':
                                        if count_el == el_parameter.count:
                                            parameter_demand = el_parameter.parameter_demand
                                        elif el_parameter.count==None:
                                            parameter_demand = el_parameter.parameter_demand
                                    elif el_parameter.count_type == 'interval':
                                        if count_el >= el_parameter.start_count_interval and count_el <= el_parameter.end_count_interval:
                                            parameter_demand = el_parameter.parameter_demand
                                    else:
                                        parameter_demand = 0

                            if id_el==1 or id_el==2:
                                Ppo=Ppo+(parameter_demand*power)
                            elif id_el==3:
                                Ppb=parameter_demand*power
                            elif id_el==4:
                                Ppc2=parameter_demand*power
                            elif id_el==5:
                                Ppc1=parameter_demand*power
                            elif id_el==6:
                                Ppc3=parameter_demand*power
                            elif id_el==7:
                                Ppc4=parameter_demand*power
                    else:
                        power = 0
                        parameter_demand = 0
                        try:
                            power = float(parts[3])
                            parameter_demand = float(parts[4])
                            count_el = int(parts[2])
                        except ValueError:
                            return HttpResponseBadRequest(
                                "Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.")
                        if count_el!=0:
                            PpcAdded = PpcAdded+(power*parameter_demand)
            else:
                return HttpResponseBadRequest(
                    "Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.")
            PpcAdded = Decimal('%s' % PpcAdded)
            PpO = Ppo + Ppb
            PpC = Ppc1 + Ppc2 + Ppc3 + Ppc4 + PpcAdded
            if PpO!=0 and PpC!=0:
                div = PpO/PpC
                if div>0.2 and div<0.75:
                    if Ppc4==0: K = 0.9
                    else: K = 0.85
                elif div>0.75 and div<1.4:
                    if Ppc4==0: K = 0.85
                    else: K = 0.75
                elif div>1.4 and div<2.5:
                    if Ppc4==0: K = 0.9
                    else: K = 0.85
                else:
                    K = 1
                K = Decimal(K)
                result = K*(PpO+PpC)
            else:
                result = False
                K = False
                div = False

            items_html = render_to_string(
                'techconnection/calc_result.html',
                    {'result': result,
                     'K':K,
                     'div':div,
                     'PpO':PpO,
                     'Ppo':Ppo,
                     'Ppb':Ppb,
                     'PpC':PpC,
                     'Ppc1':Ppc1,
                     'Ppc2':Ppc2,
                     'Ppc3':Ppc3,
                     'Ppc4':Ppc4,
                     'PpcAdded':PpcAdded
                     }
            )
            return HttpResponse(items_html)
        else:
            return HttpResponseBadRequest(
                "Произошла непредвиденная ошибка во время обработки данных. Приносим наши извинения.")

calculate = csrf_exempt(CalculateView.as_view())