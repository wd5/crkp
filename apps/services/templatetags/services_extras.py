# -*- coding: utf-8 -*-
from apps.services.models import Service
from django import template

register = template.Library()


@register.inclusion_tag("services/serv_menu.html")
def get_serv_menu(service):
    services = Service.objects.published()
    return {'services': services, 'curr_serv':service ,}

@register.simple_tag
def get_verbose_name(object,field):
    return object._meta.get_field_by_name(field)[0].verbose_name