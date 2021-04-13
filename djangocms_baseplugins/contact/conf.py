from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


TRANSLATED_FIELDS = getattr(
    settings, 'CONTACTPLUGIN_TRANSLATED_FIELDS', []
)

CONTENT_FIELDS = getattr(
    settings, 'CONTACTPLUGIN_CONTENT_FIELDS', [
        'website',
        'email',
        'phone',
        'address',
        'geocoding_address',
        'body',
    ]
)

DESIGN_FIELDS = getattr(
    settings, 'CONTACTPLUGIN_DESIGN_FIELDS', []
)

FIELDSETS = getattr(
    settings,
    'CONTACTPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

CHILD_CLASSES = getattr(
    settings, 'CONTACTPLUGIN_CHILD_CLASSES', (
        'PersonSection',
    )
)

LAYOUT_CHOICES = getattr(
    settings,
    'CONTACTPLUGIN_LAYOUT_CHOICES',
    (
        ('default', _("Default"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'CONTACTPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'CONTACTPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
