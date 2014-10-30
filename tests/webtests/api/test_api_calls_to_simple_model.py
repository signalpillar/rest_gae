# encoding: utf-8

# local
import rest_gae

# 3rd-party
from google.appengine.ext import ndb

import webapp2


config = {
    'webapp2_extras.sessions': {
        'secret_key': 'my-super-secret-key',
    }
}


class Client(ndb.Model):

    first_name = ndb.StringProperty(required=True)
    second_name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

#: Test application used to register routes under the test
TEST_APP = webapp2.WSGIApplication([
    rest_gae.RESTHandler(
        "/api/clients",
        Client,
        permissions={
            'GET': rest_gae.PERMISSION_ANYONE,
            'POST': rest_gae.PERMISSION_ANYONE,
            'PUT': rest_gae.PERMISSION_ANYONE,
            # missing DELETE in the configuration - not allowed
        },
        allow_http_method_override=False,
        allowed_origin='*',
    )
], config=config)


def test_empty_result(datastore):
    """Ensure empty document returned when there is nothing in the storage"""
    # exercise
    response = simple_get("/api/clients")
    # verify
    assert 200 == response.status_int
    assert '{"next_results_url": null, "results": []}' == response.body


def test_non_existing_resource_queried(datastore):
    """Ensure appropriate error (404) raised when resource is not found"""
    # exercise
    response = simple_get("/api/boots")
    # verify
    assert 404 == response.status_int
    assert "404 Not Found" in response.body


def simple_get(query):
    request = webapp2.Request.blank(query)
    response = request.get_response(TEST_APP)
    return response
