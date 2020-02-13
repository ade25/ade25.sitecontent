# -*- coding: utf-8 -*-
"""Module providing widget vocabularies"""
import json
from binascii import b2a_qp

from plone import api
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from ade25.widgets import MessageFactory as _


@implementer(IVocabularyFactory)
class ContentPageSectionsVocabularyFactory(object):

    def __call__(self, context):
        widgets = self.get_display_options()
        terms = [
            self.generate_simple_term(widget_key, widget_term)
            for widget_key, widget_term in widgets.items()
        ]
        return SimpleVocabulary(terms)

    @staticmethod
    def generate_simple_term(widget, widget_term):
        term = SimpleTerm(
            value=widget,
            token=b2a_qp(widget.encode('utf-8')),
            title=_(widget_term)
        )
        return term

    @staticmethod
    def get_display_options():
        display_options = {
            'page-header': _(u'Page Header'),
            'page-main': _(u'Page Main Content Area'),
            'page-footer': _(u'Page Footer')
        }
        return display_options


ContentPageSectionsVocabulary = ContentPageSectionsVocabularyFactory()
