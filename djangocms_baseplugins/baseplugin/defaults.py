# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

USE_FILER_ADDONS = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_USE_FILER_ADDONS', True
)

TRANSLATE = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_TRANSLATE', False
)

TRANSLATED_FIELDS = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS',
    ['title', 'anchor', ],
)

CONTENT_LABEL = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_CONTENT_LABEL',
    _('A - Content'),
)

CONTAINER_LABEL = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL',
    _('B - Containers'),
)

SPECIAL_LABEL = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_SPECIAL_LABEL',
    _('C - Special'),
)

ADVANCED_LABEL = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_ADVANCED_LABEL',
    _('Z - Advanced'),
)

MODE = getattr(settings, 'DJANGOCMS_BASEPLUGINS_MODE', 'default')

if MODE == 'minimal':
    advanced_fields = []
elif MODE == 'full':
    advanced_fields = [
        ['published', 'in_menu', ],
        ['published_from_date', 'published_until_date', ],
        'anchor',
    ]
else:
    advanced_fields = ['published', ]

ADVANCED_FIELDS = getattr(settings, 'DJANGOCMS_BASEPLUGINS_ADVANCED_FIELDS', advanced_fields)

WIDTH_CHOICES = getattr(
    settings, 'BASEPLUGIN_WIDTH_CHOICES',
    (
        ('', _('Automatic')),
        ('w-100', _('100%')),
        ('w-66', _('66%')),
        ('w-50', _('50%')),
        ('w-33', _('33%')),
        ('w-25', _('25%')),
    )
)


def allow_attrs_for_a(tag, name, value):
    """
    allow data-* attributes
    """
    if name.startswith('data-'):
        return True
    if name in ['href', 'target', 'title', 'rel', 'class', ]:
        return True


DEFAULT_TAGS = [
    'h1',
    'h2',
    'h3',
    'h4',
    'p',
    'span',
    'br',
    'a',
    'hr',
    'strong',
    'b',
    'em',
    'i',
    'ul',
    'ol',
    'li',
]

TABLE_TAGS = [
    'table',
    'tr',
    'th',
    'td',
]

BLEACH_CONFIG_DEFAULT = {
    'strip': True,
    'tags': DEFAULT_TAGS,
    'attributes': {
        '*': ['class', ],
        'a': allow_attrs_for_a,
    }
}

# set to None for no cleaning on save/render
# this will be passed as kwargs to the bleach.clean() method
BLEACH_CONFIG = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_BLEACH_CONFIG', None
)

# set to None for no cleaning on save/render
# this will be passed as kwargs to the lxml.html.clean.Cleaner constructor
# explanations: https://lxml.de/api/lxml.html.clean.Cleaner-class.html
LXML_CLEANER_CONFIG = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_LXML_CLEANER_CONFIG', {
        'scripts': True,
        'javascript': True,
        'comments': True,
        'style': True,
        'inline_style': True,
        'links': True,
        'meta': True,
        'page_structure': True,
        'processing_instructions': True,
        'embedded': True,
        'frames': True,
        'forms': True,
        'annoying_tags': False,
        # dont have these in basic richtext content!
        'remove_tags': ['section', 'div', 'nav', 'footer', ],
        'allow_tags': None,
        'kill_tags': None,
        'remove_unknown_tags': True,
        'safe_attrs_only': False,
        'safe_attrs': None,
        'add_nofollow': False,
        'host_whitelist': [],
        # 'whitelist_tags':
    }
)
