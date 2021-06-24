# coding: utf-8
import requests
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets
from . import conf
from .models import TweetEmbed


class TweetEmbedPluginForm(forms.ModelForm):
    class Meta:
        model = TweetEmbed
        exclude = []
        widgets = get_baseplugin_widgets(conf)


class TweetEmbedPlugin(BasePluginMixin, CMSPluginBase):
    model = TweetEmbed
    form = TweetEmbedPluginForm
    module = defaults.SPECIAL_LABEL
    name = _(u'Twitter')
    render_template = "djangocms_baseplugins/tweet_embed.html"
    fieldsets = conf.FIELDSETS

    def render(self, context, instance, placeholder):
        context = super(TweetEmbedPlugin, self).render(context, instance, placeholder)
        response = requests.get("https://publish.twitter.com/oembed?url=%s" % instance.tweet_url)
        if response.status_code == 200:
            context.update({'embed': response.json(), })
        return context


plugin_pool.register_plugin(TweetEmbedPlugin)
