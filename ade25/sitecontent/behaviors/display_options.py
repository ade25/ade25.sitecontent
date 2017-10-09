# -*- coding: utf-8 -*-
"""Module providing configuration for element display"""
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from ade25.sitecontent import MessageFactory as _


available_card_sizes = SimpleVocabulary(
    [SimpleTerm(value=u'100', title=_(u'100')),
     SimpleTerm(value=u'75', title=_(u'3/4')),
     SimpleTerm(value=u'66', title=_(u'2/3')),
     SimpleTerm(value=u'50', title=_(u'1/2')),
     SimpleTerm(value=u'33', title=_(u'1/3')),
     SimpleTerm(value=u'25', title=_(u'1/4'))
     ]
)


@provider(IFormFieldProvider)
class IDisplayOptions(model.Schema):
    """Behavior providing selectable grid sizes"""

    model.fieldset(
        'display',
        label=u"Display",
        fields=['elementSize', 'featured', 'promoted']
    )

    elementSize = schema.Choice(
        title=_(u"Select Display Size"),
        description=_(u"When displaying the content page inside a grid or "
                      u"card preview layout on a landing page the selected "
                      u"sizes will be used for alignment"),
        vocabulary=available_card_sizes,
        default=u"100",
        required=False,
    )

    featured = schema.Bool(
        title=_(u"Featured item"),
        description=_(u"Select to mark this item for featured display on "
                      u"overview pages like for example the parent container."),
        default=False,
        required=False
    )

    promoted = schema.Bool(
        title=_(u"Promote to front page"),
        description=_(u"Select to mark this item for display on the sites "
                      u"front page. Note: the number of displayed items on the "
                      u"front page might be limited or ordered by publication "
                      u"date and the selection does not force the item to be "
                      u"promoted in any case."),
        default=False,
        required=False
    )


@implementer(IDisplayOptions)
@adapter(IDexterityContent)
class DisplayOptions(object):

    def __init__(self, context):
        self.context = context
