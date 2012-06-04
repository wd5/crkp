# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url

from views import index

urlpatterns = patterns('',
    url(r'^$',index, name='index'),
    url(r'^faq/', include('apps.faq.urls')),

    url(r'^company/$', 'apps.pages.views.show_company_item', {'slug':'/about/'}),
    url(r'^company/(?P<slug>[^/]+)/$', 'apps.pages.views.show_company_item'),

    url(r'^techconnection/$', 'apps.pages.views.show_tech_item', {'slug':'/techconnect/'}),
    url(r'^techconnection/rates/$', 'apps.pages.views.show_rates_map'),
    url(r'^techconnection/(?P<slug>[^/]+)/$', 'apps.pages.views.show_tech_item'),

)
#url(r'^captcha/', include('captcha.urls')),

#urlpatterns += #app_url


