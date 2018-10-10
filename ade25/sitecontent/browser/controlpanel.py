# -*- coding: utf-8 -*-
"""Module providing controlpanels"""
from plone.app.registry.browser.controlpanel import RegistryEditForm
from zope import schema
from zope.interface import Interface
from plone.z3cform import layout
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from ade25.widgets import utils as widget_utils

from ade25.widgets import MessageFactory as _


class IAde25SiteContentControlPanel(Interface):

    widget_support_enabled = schema.Bool(
        title=_(u"Enable Widget Support"),
        description=_(u"Activate to render content elements for pages via "
                      u"predefined content widgets."),
        default=False,
        required=False,
    )

    widget_settings = schema.Text(
        title=_(u"Widget Settings JSON"),
        description=_(u"Widget configuration registry storing a string "
                      u"representation of a valid JSON settings array"),
        required=False,
        default=widget_utils.default_widget_configuration()
    )


class Ade25SiteContentControlPanelForm(RegistryEditForm):
    schema = IAde25SiteContentControlPanel
    schema_prefix = "ade25.sitecontent"
    label = u'Ade25 Site Content'


Ade25SiteContentSettings = layout.wrap_form(
    Ade25SiteContentControlPanelForm,
    ControlPanelFormWrapper
)
