# -*- coding: utf-8 -*-
"""Module providing gallery widget"""
from Acquisition import aq_inner
from Products.Five import BrowserView
from zope.component import getUtility

from ade25.base.interfaces import IResponsiveImageTool


class GalleryWidget(BrowserView):
    """ Gallery widget """

    def __call__(self,
                 widget_type='gallery',
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
        return self.render()

    def render(self):
        return self.index()

    def gallery_items(self):
        # import pdb; pdb.set_trace()
        return

    def has_image(self):
        context = aq_inner(self.context)
        try:
            lead_img = context.image
        except AttributeError:
            lead_img = None
        if lead_img is not None:
            return True
        return False

    @staticmethod
    def get_image_data(uuid):
        tool = getUtility(IResponsiveImageTool)
        return tool.create(uuid)
