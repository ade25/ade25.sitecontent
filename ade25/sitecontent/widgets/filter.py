# -*- coding: utf-8 -*-
"""Module providing content listing widgets"""
from Acquisition import aq_inner
from Products.Five import BrowserView
from plone import api
from plone.app.vocabularies.catalog import KeywordsVocabulary
from plone.i18n.normalizer import IIDNormalizer, IURLNormalizer
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
        return queryUtility(IURLNormalizer)

    def available_keywords(self):
        context = aq_inner(self.context)
        keyword_vocabulary = KeywordsVocabulary()
        vocabulary = keyword_vocabulary(context)
        return vocabulary

    def normalized_token(self, term):
        return self.normalizer().normalize(term, locale="de")

    def normalized_keywords(self):
        vocabulary = self.available_keywords()
        taxonomy = dict()
        for index, term in enumerate(vocabulary):
            element_value = term.value
            taxonomy[index] = element_value
        return taxonomy

    def filter_value(self, term):
        vocabulary = self.normalized_keywords()
        filter_value = "app-tag--undefined"
        for item_index, item_term in vocabulary.items():
            if item_term == term:
                filter_value = "app-tag--{0}".format(str(item_index))
        return filter_value

    def keyword_list(self):
        vocabulary = self.available_keywords()
        taxonomy = list()
        for term in vocabulary:
            element_value = term.value
            element_token = self.normalizer().normalize(element_value)
            taxonomy.append(element_token)
        return taxonomy


