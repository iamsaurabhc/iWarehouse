from django.db import models
from enumfields import EnumField, Enum  # Uses Ethan Furman's "enum34" backport
from django.core import serializers

'''
class NodeType(Enum):
    LOCATION = 'location'
    NAVIGATION = 'navigation'


# For G+3 warehouses
class ZoneType(Enum):
    GROUND = 'ground'
    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'


class MovementType(Enum):
    IN = 'incoming'
    OUT = 'outgoing'
'''


class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length=255)
    clientAddress = models.CharField(max_length=255)
    clientPhone = models.CharField(default=0, max_length=20)


class Product(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=255)
    productPrice = models.IntegerField(default=0)
    productDesc = models.CharField(max_length=255)
    productDimensions = models.CharField(max_length=255)


class Edge(models.Model):
    edgeID = models.AutoField(primary_key=True)
    startNode = models.IntegerField(default=0)
    endNode = models.IntegerField(default=0)
    edgeLength = models.IntegerField(default=0)


class Node(models.Model):
    nodeID = models.AutoField(primary_key=True)
    nodeName = models.CharField(max_length=255)
    nodeType = models.CharField(max_length=10)
    zone = models.CharField(max_length=7)


class Pallet(models.Model):
    palletID = models.AutoField(primary_key=True)
    nodeID = models.ForeignKey(Node, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=255)
    createDate = models.DateTimeField()


class ProductBundle(models.Model):
    bundleID = models.AutoField(primary_key=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    palletID = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    lotCode = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    dimentions = models.CharField(max_length=255)
    createDate = models.DateTimeField()


class Movement(models.Model):
    movementID = models.AutoField(primary_key=True)
    movementDate = models.DateField()
    movementType = models.CharField(max_length=9)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    productBundleID = models.ForeignKey(ProductBundle, on_delete=models.CASCADE)
    bundleQuantity = models.IntegerField(default=0)