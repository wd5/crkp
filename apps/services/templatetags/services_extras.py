# -*- coding: utf-8 -*-
from apps.services.models import Service
from django import template

register = template.Library()


@register.inclusion_tag("services/serv_menu.html")
def get_serv_menu(service):
    services = Service.objects.published().filter(second_menu_blck=False)
    return {'services': services, 'curr_serv':service ,}

@register.inclusion_tag("services/serv_menu.html")
def get_second_serv_menu(service):
    services = Service.objects.published().filter(second_menu_blck=True)
    return {'services': services, 'curr_serv':service, 'second':'second'}

@register.simple_tag
def get_verbose_name(object,field):
    return object._meta.get_field_by_name(field)[0].verbose_name

@register.filter
def show_check(value,media_root):
    if value==True:
        return "<img style='width: 0.3cm;' src='%s/media/img/1.png' />" % media_root
    elif value==False:
        return "<img style='width: 0.3cm;' src='%s/media/img/0.png' />" % media_root
