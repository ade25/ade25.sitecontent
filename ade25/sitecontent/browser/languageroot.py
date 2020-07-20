# -*- coding: utf-8 -*-
"""Module providing views for the folderish content page type"""
from Acquisition import aq_inner
from Products.CMFCore.interfaces import ISiteRoot
from Products.Five.browser import BrowserView
from ade25.base.utils import get_acquisition_chain
from ade25.sitecontent.languagefolder import ILanguageFolder
from plone import api
from plone.app.z3cform.utils import replace_link_variables_by_paths


class LanguageRootView(BrowserView):
    """ Site section default view """

    def __call__(self):
        if api.user.is_anonymous() and self.has_link_action():
            link_target = self.get_link_action()
            self.request.response.redirect(link_target)
        else:
            return self.render()

    def render(self):
        return self.index()

    def panel_page_support_enabled(self):
        context = aq_inner(self.context)
        try:
            from ade25.panelpage.behaviors.storage import IContentPanelStorage
            if IContentPanelStorage.providedBy(context):
                return True
            else:
                return False
        except ImportError:
            return False

    def has_link_action(self):
        context = aq_inner(self.context)
        try:
            context_link = context.link
        except AttributeError:
            context_link = None
        if context_link is not None:
            return True
        return False

    def get_link_action(self):
        context = aq_inner(self.context)
        link = context.link
        link_action = replace_link_variables_by_paths(context, link)
        return link_action

    @staticmethod
    def is_authenticated():
        return not api.user.is_anonymous()


class LanguageRootSwitcher(BrowserView):
    """ Site root language switcher """

    @staticmethod
    def available_languages():
        languages = list()
        default_title = api.portal.translate(
            "DE",
            'ade25.sitecontent',
            api.portal.get_current_language()
        )
        languages.append(
            {
                "id": "de",
                "title": default_title,
                "url": api.portal.get().absolute_url()
            }
        )
        brains = api.content.find(
            context=api.portal.get(),
            depth=1,
            object_provides=ILanguageFolder,
        )
        for brain in brains:
            languages.append({
                "id": brain.getId,
                "title": brain.Title,
                "url": brain.getURL()
            })
        return languages

    @staticmethod
    def active_language(item_uid):
        context = api.content.get(UID=item_uid)
        default_language = 'de'
        if ISiteRoot.providedBy(context):
            return default_language
        acquisition_chain = get_acquisition_chain(context)
        for node in acquisition_chain:
            if ILanguageFolder.providedBy(node):
                return node.getId
        return default_language
