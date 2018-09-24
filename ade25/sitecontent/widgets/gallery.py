# -*- coding: utf-8 -*-
"""Module providing base widget"""
from Products.Five import BrowserView


class GallerySliderWidgetView(BrowserView):
    """ Base widget used as placeholder """

    def __call__(self):
        return self.render()

    def render(self):
        return self.index()
