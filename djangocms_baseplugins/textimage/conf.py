# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TEXTIMAGEPLUGIN_CLEAN_ON_SAVE = getattr(
    settings,
    'TEXTIMAGEPLUGIN_CLEAN_ON_SAVE',
    True,
)

TEXTIMAGEPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'TEXTIMAGEPLUGIN_TRANSLATED_FIELDS', [
        'caption', 'body',
    ]
)

TEXTIMAGEPLUGIN_LAYOUT_CHOICES = getattr(
    settings, 'TEXTIMAGEPLUGIN_LAYOUT_CHOICES', (
        [],
    )
)

TEXTIMAGEPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'TEXTIMAGEPLUGIN_CONTENT_FIELDS', (
        'image', 'caption', 'body',
    )
)

TEXTIMAGEPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'TEXTIMAGEPLUGIN_DESIGN_FIELDS', []
)

TEXTIMAGEPLUGIN_FIELDSETS = getattr(
    settings,
    'TEXTIMAGEPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': TEXTIMAGEPLUGIN_DESIGN_FIELDS,
        'content': TEXTIMAGEPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)


TEXTIMAGEPLUGIN_IMAGE_REQUIRED = getattr(
    settings, 'TEXTIMAGEPLUGIN_IMAGE_REQUIRED', True
)
