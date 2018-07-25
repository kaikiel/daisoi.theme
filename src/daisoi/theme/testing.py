# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import daisoi.theme


class DaisoiThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=daisoi.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'daisoi.theme:default')


DAISOI_THEME_FIXTURE = DaisoiThemeLayer()


DAISOI_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DAISOI_THEME_FIXTURE,),
    name='DaisoiThemeLayer:IntegrationTesting'
)


DAISOI_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DAISOI_THEME_FIXTURE,),
    name='DaisoiThemeLayer:FunctionalTesting'
)


DAISOI_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DAISOI_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DaisoiThemeLayer:AcceptanceTesting'
)
