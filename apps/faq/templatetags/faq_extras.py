# -*- coding: utf-8 -*-
from django import template
from apps.siteblocks.models import Settings

register = template.Library()

@register.inclusion_tag("faq/faq_teaser.html")
def faq_teaser(type):
    try:
        faq_teaser_text = Settings.objects.get(name='faq_teaser_text').value
    except Settings.DoesNotExist:
        faq_teaser_text = ''
    return {'type': type, 'faq_teaser_text':faq_teaser_text, }