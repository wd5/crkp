# -*- coding: utf-8 -*-
from AptUrl.Helpers import _
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from apps.services.models import Service
from django.views.generic import ListView,DetailView,TemplateView

class ShowServiceView(DetailView):
    model = Service
    template_name = 'services/show_service.html'
    context_object_name = 'service'

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

show_service = ShowServiceView.as_view()
