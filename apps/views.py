# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from apps.siteblocks.models import Settings, MainTeaser

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            context['maintxt_first'] = Settings.objects.get(name="main_first")
        except Settings.DoesNotExist:
            context['maintxt_first'] = False
        try:
            context['maintxt_second'] = Settings.objects.get(name="main_second")
        except Settings.DoesNotExist:
            context['maintxt_first'] = False

        context['teasers'] = MainTeaser.objects.published()
        return context

index = IndexView.as_view()

from apps.utils.utils import render_to_pdf
from apps.servicerequests.models import FifthServRequest, SecondServRequest, ThirdServRequest, FourthServRequest, FirstServRequest
import settings

class GP(TemplateView):
    template_name = 'pages/default.html'

    def get_context_data(self, **kwargs):
        context = super(GP, self).get_context_data(**kwargs)
        s_object = FirstServRequest.objects.get(id=1)
        path = render_to_pdf('services/pdf.html', '11111', {
            'title': u'Физические лица до 15 кВт (включительно) по 3 категории надежности электроснабжения',
            'saved_object': s_object,
            'case': 'first_serv',
            'MEDIA_ROOT': settings.ROOT_PATH
        })

        s_object = SecondServRequest.objects.get(id=1)
        path = render_to_pdf('services/pdf.html', '22222', {
            'title': u'Физические лица до 100 кВт (включительно) по 1,2,3 категории надежности электроснабжения ВРЕМЕННОЕ присоединение'
            ,
            'saved_object': s_object,
            'case': 'second_serv',
            'MEDIA_ROOT': settings.ROOT_PATH
        })

        s_object = ThirdServRequest.objects.get(id=1)
        path = render_to_pdf('services/pdf.html', '33333', {
            'title': u'Юридические лица и индивидуальные предприниматели до 100 кВт (включительно) по 1, 2, 3 категории надежности электроснабжения ВРЕМЕННОЕ присоединение'
            ,
            'saved_object': s_object,
            'case': 'third_serv',
            'MEDIA_ROOT': settings.ROOT_PATH
        })

        s_object = FourthServRequest.objects.get(id=1)
        path = render_to_pdf('services/pdf.html', '44444', {
            'title': u'Юридические лица и индивидуальные предприниматели до 750 кВА (включительно) по 1, 2, 3 категории надежности электроснабжения'
            ,
            'saved_object': s_object,
            'case': 'fourth_serv',
            'MEDIA_ROOT': settings.ROOT_PATH
        })

        s_object = FifthServRequest.objects.get(id=1)
        path = render_to_pdf('services/pdf.html', '55555', {
            'title': u'Юридические лица и индивидуальные предприниматели свыше 750 кВА по 1,2,3 категории надежности электроснабжения'
            ,
            'saved_object': s_object,
            'case': 'fifth_serv',
            'MEDIA_ROOT': settings.ROOT_PATH
        })
        return context

generatepdf = GP.as_view()