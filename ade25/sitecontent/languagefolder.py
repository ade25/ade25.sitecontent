# -*- coding: utf-8 -*-
"""Module providing section container content type"""
from plone.app.z3cform.widget import LinkFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implementer

from ade25.sitecontent import MessageFactory as _


class ILanguageFolder(model.Schema, IImageScaleTraversable):
    """
    Folder to represent the site sections
    """

    fieldset(
        'redirect',
        label=u"Redirect",
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

    fieldset(
        'media',
        label=_(u"Media"),
        fields=['image', 'image_caption']
    )

    image = NamedBlobImage(
        title=_(u"Banner and Preview Image"),
        description=_(u"Upload preview image that can be used in search "
                      u"results and listings and act as a content cover."),
        required=False
    )

    image_caption = schema.TextLine(
        title=_(u"Cover Image Caption"),
        required=False
    )

    fieldset(
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


@implementer(ILanguageFolder)
class LanguageFolder(Container):

    def canSetDefaultPage(self):
        return False
