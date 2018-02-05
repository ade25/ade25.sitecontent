# -*- coding: utf-8 -*-
"""Module providing section folder content type"""
from plone.app.z3cform.widget import LinkFieldWidget
from plone.dexterity.content import Container
from plone.directives import form
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
        label=u"Redirect",
        fields=['link', ]
    )

    form.widget(link=LinkFieldWidget)
    link = schema.TextLine(
        title=_(u"Link"),
        description=_(u"Optional internal or external link that will be "
                      u"used as redirection target when section is accessed."
                      u"Logged in users will see the target link instead."),
        required=False,
    )


@implementer(ISectionFolder)
class SectionFolder(Container):

    def canSetDefaultPage(self):
        return False
