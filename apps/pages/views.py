# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template
from apps.pages.models import Page, Vacancy, LicensesCategory
from apps.siteblocks.models import Settings
from django.utils.translation import ugettext as _
from django.views.generic import ListView,DetailView,TemplateView

def page(request, url):
    if not url.endswith('/'):
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    page = get_object_or_404(Page, url__exact=url)
    return direct_to_template(request, 'pages/default.html', locals())

@csrf_exempt
def static_page(request, template):
    return direct_to_template(request, template, locals())

class ShowCompItemView(DetailView):
    slug_field = 'url'
    model = Page
    template_name = 'pages/company_blocks.html'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super(ShowCompItemView,self).get_context_data(**kwargs)
        if context['page'].url == '/contacts/':
            context['contacts_page_block'] = Settings.objects.get(name="contacts_page_block")
        if context['page'].url == '/vacancies/':
            context['vacancies'] = Vacancy.objects.published()
        if context['page'].url == '/license/':
            context['licCategories'] = LicensesCategory.objects.published()
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        elif slug is not None:
            if not slug.endswith('/'):
                slug += '/'
            if not slug.startswith('/'):
                slug = "/" + slug
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

show_company_item = ShowCompItemView.as_view()