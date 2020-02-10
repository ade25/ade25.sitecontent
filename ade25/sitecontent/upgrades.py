# -*- coding: utf-8 -*-
# Module providing version specific upgrade steps
import logging

default_profile = 'profile-ade25.sitecontent:default'
logger = logging.getLogger(__name__)


def upgrade_1001(setup):
    setup.runImportStepFromProfile(default_profile, 'typeinfo')
    setup.runImportStepFromProfile(default_profile, 'controlpanel')
    # Update registry settings
    setup.runImportStepFromProfile(default_profile, 'plone.app.registry')
