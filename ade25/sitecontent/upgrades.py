# -*- coding: utf-8 -*-
"""Module providing custom upgrade functions"""
from plone import api
import logging

PROFILE_ID = 'profile-ade25.sitecontent:default'


def setup_package_widget(site, logger=None):
    """Method to add widget setup to global widget registry

    @param site: Plone site
    """
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('ade25.sitecontent')

    widget_types = ['Gallery Slider',
                    'Gallery Thumbnail Slider',
                    'Gallery Image Cards']
    listed_types = api.portal.get_registry_record(
        name='ade25.widgets.widget_types'
    )
    for content_type in widget_types:
        if content_type not in listed_types:
            listed_types.append(content_type)
    api.portal.set_registry_record(
        name='ade25.widgets.widget_types',
        value=listed_types
    )
    logger.info('Add 3 content widgets to registry')
