# -*- coding: utf-8 -*-
"""Module providing section folder content type"""
from plone.app.z3cform.widget import LinkFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.interface import implementer
from zope import schema

from ade25.sitecontent import MessageFactory as _


class ISectionFolder(model.Schema, IImageScaleTraversable):
    """
    A folder acting as dedicated site section
    """

    model.fieldset(
        'redirect',
        label=_(u"Redirect"),
        fields=['link', ]
    )

    directives.widget(link=LinkFieldWidget)
    link = schema.TextLine(
        title=_(u"Link"),
        description=_(u"Optional internal or external link that will be "
                      u"used as redirection target when section is accessed."
                      u"Logged in users will see the target link instead."),
        required=False,
    )

    model.fieldset(
        'settings',
        label=_(u"Settings"),
        fields=['display_page_header', ]
    )

    display_page_header = schema.Bool(
        title=_(u"Display page header"),
        description=_(u"When activated the view will display a page header consisting "
                      u"of the default title and description. It is recommended to "
                      u"to use a page header widget for display and tread the objects"
                      u"title and description as metadata. This allows for short "
                      u"navigation titles and can be used for search engine "
                      u"optimization."),
        required=False,
        default=False,
    )


@implementer(ISectionFolder)
class SectionFolder(Container):

    def canSetDefaultPage(self):
        return False
