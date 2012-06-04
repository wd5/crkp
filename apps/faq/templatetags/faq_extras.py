# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag("faq/faq_teaser.html")
def faq_teaser(type):
    return {'type':type}