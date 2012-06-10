# -*- coding: utf-8 -*-
DATABASE_NAME = u'crkp'
PROJECT_NAME = u'crkp'
SITE_NAME = u'ЦРКП'
DEFAULT_FROM_EMAIL = u'support@crkp.octweb.ru'

from config.base import *

try:
    from config.development import *
except ImportError:
    from config.production import *

TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'apps.siteblocks',
    'apps.pages',
    'apps.faq',
    'apps.services',
    'apps.servicerequests',
    'apps.techconnection',


    'sorl.thumbnail',
    #'south',
    #'captcha',
)

MIDDLEWARE_CLASSES += (
    'apps.pages.middleware.PageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'apps.pages.context_processors.meta',
    'apps.siteblocks.context_processors.settings',
)