# -*- coding: utf-8 -*-
"""Module providing custom setup steps"""
from plone import api


def register_content_types(site):
    """Run custom add-on package installation code to modify Plone
       site object and others

    @param site: Plone site
    """
    navigation_types = ['ade25.sitecontent.sectionfolder', ]
    listed_types = api.portal.get_registry_record(
        name='ade25.base.listed_content_types'
    )
    for content_type in navigation_types:
        if content_type not in listed_types:
            listed_types.append(content_type)
    api.portal.set_registry_record(
        name='ade25.base.listed_content_types',
        value=listed_types
    )


def register_widget_types(site):
    """Add content widgets provided by this package to global widget registry

    @param site: Plone site
    """
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


def setup_various(context):
    """
    @param context: Products.GenericSetup.context.DirectoryImportContext instance
    """

    # We check from our GenericSetup context whether we are running
    # add-on installation for your package or any other
    if context.readDataFile('ade25.sitecontent.marker.txt') is None:
        # Not your add-on
        return

    portal = context.getSite()

    register_content_types(portal)

    register_widget_types(portal)
