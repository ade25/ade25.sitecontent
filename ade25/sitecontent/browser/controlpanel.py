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

    editable_content_widgets = schema.List(
        title=_(u"Editable Page Sections"),
        description=_(u"Select the page sections that allow editors "
                      u"content widget managements."),
        value_type=schema.Choice(
            vocabulary='ade25.sitecontent.vocabularies.ContentPageSections'
        ),
        default=['page-main', ],
        required=False
    )


class Ade25SiteContentControlPanelForm(RegistryEditForm):
    schema = IAde25SiteContentControlPanel
    schema_prefix = "ade25.sitecontent"
    label = u'Ade25 Site Content'


Ade25SiteContentSettings = layout.wrap_form(
    Ade25SiteContentControlPanelForm,
    ControlPanelFormWrapper
)
