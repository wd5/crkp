# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url
from django.views.decorators.csrf import csrf_exempt
from apps.services.views import load_serv
from apps.servicerequests.views import load_request_form,check_request_form

from views import index

urlpatterns = patterns('',
    url(r'^$',index, name='index'),
    (r'^faq/', include('apps.faq.urls')),

    (r'^company/$', 'apps.pages.views.show_company_item', {'slug':'/about/'}),
    (r'^company/(?P<slug>[^/]+)/$', 'apps.pages.views.show_company_item'),

    (r'^techconnection/$', 'apps.techconnection.views.show_tech_item', {'slug':'/techconnect/'}),
    (r'^techconnection/rates/$', 'apps.techconnection.views.show_rates_map'),
    (r'^techconnection/techcalc/$', 'apps.techconnection.views.show_techcalc'),
    (r'^techconnection/(?P<slug>[^/]+)/$', 'apps.techconnection.views.show_tech_item'),
    (r'^showratestable/(?P<slug>[^/]+)/$', 'apps.techconnection.views.show_rates_table'),

    (r'^services/loadsrv/$', csrf_exempt(load_serv)),
    (r'^services/checkform/$',csrf_exempt(check_request_form)),
    (r'^services/requestform/(?P<id>[^/]+)/$', csrf_exempt(load_request_form)),
    url(r'^services/$', 'apps.services.views.show_service', {'pk':'1'}, name='show_service'),
    (r'^services/(?P<pk>[^/]+)/$', 'apps.services.views.show_service'),

)

