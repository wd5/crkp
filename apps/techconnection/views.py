# -*- coding: utf-8 -*-
from AptUrl.Helpers import _
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from apps.pages.models import Page
from apps.techconnection.models import MapPolygon
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

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        elif slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        else:
            raise AttributeError(u"Generic detail view %s must be called with "
                                 u"either an object pk or a slug."
                                 % self.__class__.__name__)

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_(u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

show_rates_table = ShowRatesTableView.as_view()
