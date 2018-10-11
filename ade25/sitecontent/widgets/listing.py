# -*- coding: utf-8 -*-
"""Module providing content listing widgets"""
from Acquisition import aq_inner
from Products.Five import BrowserView
from plone import api


class BaseListingWidget(BrowserView):
    """ Basic context content listing """

    def __call__(self,
                 widget_type='listing-base',
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
        self.has_content = len(self.contained_content_items()) > 0
        return self.render()

    def render(self):
        return self.index()

    def content_items(self):
        results = []
        brains = self.contained_content_items()
        for brain in brains:
            results.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': brain.getURL(),
                'timestamp': brain.Date,
                'uuid': brain.UID
            })
        return results

    def contained_content_items(self):
        items = api.content.find(
            context=aq_inner(self.context),
            depth=1,
            portal_type=['ContentPage', 'SectionFolder'],
            review_state='published',
            sort_on='getObjPositionInParent'
        )
        return items
