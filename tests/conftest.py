# encoding: utf-8

from google.appengine.ext import testbed

import pytest

#: Default aplication ID used for the testing purposes.
DEFAULT_APP_ID = "default-app-id-for-testing"


@pytest.yield_fixture
def datastore():
    """Create an instance of testbed with datastore stubbed"""
    inst = testbed.Testbed()
    inst.activate()
    inst.setup_env(app_id=DEFAULT_APP_ID)
    inst.init_datastore_v3_stub()
    yield inst
    inst.deactivate()
