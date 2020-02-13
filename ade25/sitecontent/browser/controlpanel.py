# -*- coding: utf-8 -*-
"""Module providing controlpanels"""
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.autoform import directives as form
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

    lead_image_scale = schema.Choice(
        title=_(u"Content Page Lead Image Scale"),
        vocabulary='ade25.widgets.vocabularies.AvailableImageScales',
        default='ratio-4:3',
        required=False
    )
    lead_image_aspect_ratio = schema.TextLine(
        title=_(u"Content Page Lead Image Aspect Ratio (optional)"),
        default='4/3',
        required=False
    )

    form.widget('display_columns', klass='js-choices-selector')
    display_columns = schema.Choice(
        title=_(u"Listing Layout"),
        description=_(u"Select the number of cards that should be displayed "
                      u"per column if the screen size allows for horizontal "
                      u"alignment."),
        required=False,
        default='width-33',
        vocabulary='ade25.widgets.vocabularies.ContentWidgetLayoutOptions'
    )
    listing_cards_scale = schema.Choice(
        title=_(u"Content Listing Cards: Image Scale"),
        vocabulary='ade25.widgets.vocabularies.AvailableImageScales',
        default='ratio-4:3',
        required=False
    )
    display_read_more = schema.Bool(
        title=_(u"Display Read More Link"),
        default=True,
        required=False
    )
    read_more_text = schema.TextLine(
        title=_(u"Read More Text"),
        description=_(u"Enter displayed text for read more element."),
        default=_(u'Read more'),
        required=False
    )
    form.widget('read_more_layout', klass='js-choices-selector')
    read_more_layout = schema.Choice(
        title=_(u"Read More Layout"),
        description=_(u"Select how the card footer link should be displayed."),
        required=False,
        default='link',
        vocabulary='ade25.widgets.vocabularies.ContentWidgetReadMeLayoutOptions'
    )


class Ade25SiteContentControlPanelForm(RegistryEditForm):
    schema = IAde25SiteContentControlPanel
    schema_prefix = "ade25.sitecontent"
    label = u'Ade25 Site Content'


Ade25SiteContentSettings = layout.wrap_form(
    Ade25SiteContentControlPanelForm,
    ControlPanelFormWrapper
)
