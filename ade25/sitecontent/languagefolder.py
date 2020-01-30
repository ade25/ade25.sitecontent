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

from adk.site import _


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


@implementer(ILanguageFolder)
class LanguageFolder(Container):

    def canSetDefaultPage(self):
        return False
