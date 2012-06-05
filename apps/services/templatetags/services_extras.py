# -*- coding: utf-8 -*-
from apps.services.models import Service
from django import template

register = template.Library()


@register.inclusion_tag("services/serv_menu.html")
def get_serv_menu(service):
    services = Service.objects.published()
    return {'services': services, 'curr_serv':service ,}