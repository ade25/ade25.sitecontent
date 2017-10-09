# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class IAde25SitecontentLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IResponsiveImagesTool(Interface):
    """ Responsive image generator

        General tool providing srcset compatible image transforms
    """

    def create(context):
        """ Create a set of image scales

        The caller is responsible for passing a valid data dictionary
        containing the necessary details

        Returns dictionary of available scales

        @param uuid:            content object UID
        @param image_field:     content object image field (default: image)
        """
