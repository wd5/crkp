# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url
from django.views.decorators.csrf import csrf_exempt
from apps.services.views import load_serv
from apps.servicerequests.views import load_request_form,check_request_form

from views import index

urlpatterns = patterns('',
    url(r'^$',index, name='index'),
    url(r'^faq/', include('apps.faq.urls')),

    url(r'^company/$', 'apps.pages.views.show_company_item', {'slug':'/about/'}),
    url(r'^company/(?P<slug>[^/]+)/$', 'apps.pages.views.show_company_item'),

    url(r'^techconnection/$', 'apps.techconnection.views.show_tech_item', {'slug':'/techconnect/'}),
    url(r'^techconnection/rates/$', 'apps.techconnection.views.show_rates_map'),
    url(r'^techconnection/(?P<slug>[^/]+)/$', 'apps.techconnection.views.show_tech_item'),
    url(r'^showratestable/(?P<slug>[^/]+)/$', 'apps.techconnection.views.show_rates_table'),

    url(r'^services/loadsrv/$', csrf_exempt(load_serv)),
    url(r'^services/checkform/$',csrf_exempt(check_request_form)),
    url(r'^services/requestform/(?P<id>[^/]+)/$', csrf_exempt(load_request_form)),
    url(r'^services/$', 'apps.services.views.show_service', {'pk':'1'}, name='show_service'),
    url(r'^services/(?P<pk>[^/]+)/$', 'apps.services.views.show_service'),


)
#url(r'^captcha/', include('captcha.urls')),

#urlpatterns += #app_url


