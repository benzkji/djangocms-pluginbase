# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_fields_from_fieldsets, get_baseplugin_widgets
from . import conf
from .models import Section


class SectionPluginForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = get_fields_from_fieldsets(conf.FIELDSETS)
        # exclude = []
        widgets = get_baseplugin_widgets(conf)


class SectionPlugin(BasePluginMixin, CMSPluginBase):
    model = Section
    form = SectionPluginForm
    module = defaults.CONTAINER_LABEL
    name = _(u'Section')
    render_template = "djangocms_baseplugins/section.html"
    fieldsets = conf.FIELDSETS
    allow_children = True
    child_classes = conf.CHILD_CLASSES


plugin_pool.register_plugin(SectionPlugin)
