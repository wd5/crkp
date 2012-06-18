# -*- coding: utf-8 -*-
from apps.pages.models import Page
from django import template

register = template.Library()

@register.inclusion_tag("pages/block_page_summary.html")
def block_page_summary(alias):
    try:
        page = Page.objects.get(url = alias)
        return {'page': page}
    except Page.DoesNotExist:
        return {}

@register.inclusion_tag("pages/menu_by_parent.html")
def get_menu_by_parent(page,current_path):
    return {'children_pages': page.parent.get_children().filter(is_published=True), 'current_path':current_path,'page_url':page.get_absolute_url() }