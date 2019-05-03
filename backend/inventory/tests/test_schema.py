import pytest
from mixer.backend.django import mixer
from graphql_relay.node.node import to_global_id
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory


from .. import schema


pytestmark = pytest.mark.django_db


'''
Test for Model returns
'''


def test_client_type():
    instance = schema.ClientType()
    assert instance


def test_product_type():
    instance = schema.ProductType()
    assert instance


def test_edge_type():
    instance = schema.EdgeType()
    assert instance


def test_node_type():
    instance = schema.NodeType()
    assert instance


def test_pallet_type():
    instance = schema.ProductBundleType()
    assert instance


def test_productbundle_type():
    instance = schema.ProductBundleType()
    assert instance


def test_movement_type():
    instance = schema.MovementType()
    assert instance


'''
Test for Queries
'''


def test_resolve_all_clients():
    mixer.blend('inventory.Client')
    mixer.blend('inventory.Client')
    q = schema.Query()
    res = q.resolve_all_clients(None, None, None)
    assert res.count() == 2, 'Should return all clients'


def test_resolve_client():
    client = mixer.blend('inventory.Client')
    q = schema.Query()
    clientID = to_global_id('ClientType', client.pk)
    res = q.resolve_client({'id': clientID}, None, None)
    assert res == client, 'Should return the requested client'

# Other tests needs to be defined

'''
Mutation Tests
'''


def test_create_message_mutation():
    user = mixer.blend('auth.User')
    mut = schema.CreateMessageMutation()

    data = {'message': 'Test'}
    req = RequestFactory().get('/')
    req.user = AnonymousUser()
    res = mut.mutate(None, data, req, None)
    assert res.status == 403, 'Should return 403 if user is not logged in'

    req.user = user
    res = mut.mutate(None, {}, req, None)
    assert res.status == 400, 'Should return 400 if there are form errors'
    assert 'message' in res.formErrors, (
        'Should have form error for message field')

    res = mut.mutate(None, data, req, None)
    assert res.status == 200, 'Should return 200 if mutation is successful'
    assert res.message.pk == 1, 'Should create new message'