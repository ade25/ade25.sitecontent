# -*- coding: utf-8 -*-
"""Module providing preview cards"""
from Acquisition import aq_inner
from Products.Five import BrowserView
from plone import api


class ContextCardWidget(BrowserView):
    """ Basic context content card """

    def __call__(self,
                 widget_data=None,
                 widget_mode='view',
                 **kw):
        self.params = {
            'widget_mode': widget_mode,
            'widget_data': widget_data
        }
        return self.render()

    def render(self):
        return self.index()

    @staticmethod
    def can_edit():
        return not api.user.is_anonymous()

    @staticmethod
    def has_image(context):
        try:
            lead_img = context.image
        except AttributeError:
            lead_img = None
        if lead_img is not None:
            return True
        return False

    def widget_content(self):
        context = aq_inner(self.context)
        widget_data = self.params['widget_data']
        if 'uuid' in widget_data:
            context = api.content.get(UID=widget_data['uuid'])
        details = {
            'title': context.Title(),
            'description': context.Description(),
            'url': context.absolute_url(),
            'timestamp': context.Date,
            'uuid': context.UID,
            'has_image': self.has_image(context),
            'content_item': context
        }
        return details
