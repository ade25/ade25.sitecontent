# -*- coding: utf-8 -*-
"""Module providing content listing widgets"""
from Acquisition import aq_inner
from Products.Five import BrowserView
from plone import api
from plone.app.vocabularies.catalog import KeywordsVocabulary
from plone.i18n.normalizer import IIDNormalizer
from zope.component import queryUtility


class KeywordFilterWidget(BrowserView):
    """ Basic context content listing """

    def __call__(self,
                 widget_type='filter-keywords',
                 identifier=None,
                 data_set=None,
                 widget_mode='view',
                 **kw):
        self.params = {
            'widget_name': identifier,
            'widget_type': widget_type,
            'widget_mode': widget_mode,
            'widget_data': data_set
        }
        self.has_content = True
        return self.render()

    def render(self):
        return self.index()

    @staticmethod
    def normalizer():
        return queryUtility(IIDNormalizer)

    def available_keywords(self):
        context = aq_inner(self.context)
        keyword_vocabulary = KeywordsVocabulary()
        vocabulary = keyword_vocabulary(context)
        return vocabulary

    def normalized_token(self, term):
        return self.normalizer().normalize(term)

    def normalized_keywords(self):
        vocabulary = self.available_keywords()
        taxonomy = dict()
        for term in vocabulary:
            element_value = term.value
            element_token = self.normalizer().normalize(element_value)
            taxonomy[element_token] = element_value
        return taxonomy

    def keyword_list(self):
        vocabulary = self.available_keywords()
        taxonomy = list()
        for term in vocabulary:
            element_value = term.value
            element_token = self.normalizer().normalize(element_value)
            taxonomy.append(element_token)
        return taxonomy


