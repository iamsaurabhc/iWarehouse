import pytest
from mixer.backend.django import mixer

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db

'''
Test for all models
'''


def test_client():
    obj = mixer.blend('inventory.Client')
    assert obj.pk > 0


def test_product():
    obj = mixer.blend('inventory.Product')
    assert obj.pk > 0


def test_edge():
    obj = mixer.blend('inventory.Edge')
    assert obj.pk > 0


def test_node():
    obj = mixer.blend('inventory.Node')
    assert obj.pk > 0


def test_pallet():
    obj = mixer.blend('inventory.Pallet')
    assert obj.pk > 0


def test_productbundle():
    obj = mixer.blend('inventory.ProductBundle')
    assert obj.pk > 0


def test_movement():
    obj = mixer.blend('inventory.Movement')
    assert obj.pk > 0
