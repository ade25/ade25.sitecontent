# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from ade25.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of ade25.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ade25.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.ade25roductInstalled('ade25.sitecontent'))

    def test_uninstall(self):
        """Test if ade25.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['ade25.sitecontent'])
        self.assertFalse(self.installer.ade25roductInstalled('ade25.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IAde25SitecontentLayer is registered."""
        from ade25.sitecontent.interfaces import IAde25SitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IAde25SitecontentLayer in utils.registered_layers())
