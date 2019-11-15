# -*- coding: utf-8 -*-
"""Module providing widget settings"""

from zope import schema
from zope.interface import Interface

from ade25.widgets import MessageFactory as _


class IAde25SiteContentWidgets(Interface):

    card = schema.TextLine(
        title=_(u"Widget: Card"),
        required=False,
    )
