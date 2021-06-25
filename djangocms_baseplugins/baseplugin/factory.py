from cms.plugin_base import CMSPluginBase
from django import forms

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.forms import BasePluginFormMixin
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets, get_fields_from_fieldsets
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin


def baseplugin_classfactory(model_class, conf, form=None, more_mixin_classes=list()):
    class_name = model_class.__name__
    super_classes = more_mixin_classes + [BasePluginMixin, CMSPluginBase]
    super_classes = tuple(super_classes)
    if not form:
        form = baseplugin_formfactory(model_class, conf)
    module, sep, tail = model_class.__module__.rpartition('.models')
    attrs = {
        '__module__': module + '.cms_plugins',
        'model': model_class,
        'form': form,
        'module': getattr(conf, 'MODULE', defaults.CONTENT_LABEL),
        'name': getattr(conf, 'NAME', class_name),
        'render_template': "djangocms_baseplugins/{}.html".format(class_name.lower()),
        'fieldsets': getattr(conf, 'FIELDSETS', []),
        'allow_children': getattr(conf, 'ALLOW_CHILDREN', False),
        'child_classes': getattr(conf, 'CHILD_CLASSES', None),
        'require_parent': getattr(conf, 'REQUIRE_PARENT', False),
    }
    cls = type('{}Plugin'.format(class_name), super_classes, attrs)
    return cls


def baseplugin_formfactory(model_class, conf):
    # build meta inner class
    fields = get_fields_from_fieldsets(conf.FIELDSETS)
    meta_attrs = {
        'model': model_class,
        'fields': fields,
        'widgets': get_baseplugin_widgets(conf),
        'labels': {},
        'help_texts': {},
    }
    for field in fields:
        key = 'LABEL_{}'.format(field.upper())
        value = getattr(conf, key, None)
        if value:
            meta_attrs['labels'][key] = value
        key = 'HELP_TEXT_{}'.format(field.upper())
        value = getattr(conf, key, None)
        if value:
            meta_attrs['help_texts'][key] = value
    meta = type('Meta', (BasePluginFormMixin, forms.ModelForm, ), meta_attrs)
    # build form class itself
    form_attrs = {
        'Meta': meta,
    }
    return type('{}PluginForm', (forms.ModelForm, ), form_attrs)
