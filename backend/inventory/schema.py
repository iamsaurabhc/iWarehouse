import graphene
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id
import json

from . import models

'''
Model Returns
'''


class ClientType(DjangoObjectType):
    class Meta:
        model = models.Client
        interfaces = (graphene.Node, )


class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product
        interfaces = (graphene.Node, )


class EdgeType(DjangoObjectType):
    class Meta:
        model = models.Edge
        interfaces = (graphene.Node, )


class NodeType(DjangoObjectType):
    class Meta:
        model = models.Node
        interfaces = (graphene.Node, )


class PalletType(DjangoObjectType):
    class Meta:
        model = models.Pallet
        interfaces = (graphene.Node, )


class ProductBundleType(DjangoObjectType):
    class Meta:
        model = models.ProductBundle
        interfaces = (graphene.Node, )


class MovementType(DjangoObjectType):
    class Meta:
        model = models.Movement
        interfaces = (graphene.Node, )


'''
Query Returns
'''


class Query(object):
    '''
    Clients Queries
    '''

    all_clients = graphene.List(ClientType)
    client = graphene.Field(ClientType, clientID=graphene.ID())

    def resolve_all_clients(self, args):
        return models.Client.objects.all()

    def resolve_client(self, info, clientID):
        return models.Client.objects.get(pk=clientID)

    '''
    Products Queries
    '''
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, productID=graphene.ID())

    def resolve_all_products(self, args):
        return models.Product.objects.all()
    
    def resolve_product(self, info, productID):
        return models.Product.objects.get(pk=productID)

    '''
    Product Bundle Queries
    '''
    all_product_bundles = graphene.List(ProductBundleType)
    product_bundle = graphene.Field(ProductBundleType, bundleID=graphene.ID())

    def resolve_all_product_bundles(self, args):
        return models.ProductBundle.objects.all()
    
    def resolve_product_bundle(self, info, bundleID):
        return models.ProductBundle.objects.get(pk=bundleID)

    '''
    Pallet Queries
    '''
    all_pallets = graphene.List(PalletType)
    pallet = graphene.Field(PalletType, palletID=graphene.ID())

    def resolve_all_pallets(self, args):
        return models.Pallet.objects.all()

    def resolve_pallet(self, info, palletID):
        return models.Pallet.objects.get(pk=palletID)
    
    '''
    Movement Queries
    '''
    all_movements = graphene.List(MovementType)
    movement = graphene.Field(MovementType, movementID=graphene.ID())

    def resolve_all_movements(self, args):
        return models.Movement.objects.all()
    
    def resolve_movement(self, info, movementID):
        return models.Movement.objects.get(pk=movementID)

'''
Mutation
'''


class CreateMessageMutation(graphene.Mutation):
    class Input:
        clientName = graphene.String()
        clientAddress = graphene.String()
        clientPhone = graphene.String()

    status = graphene.Int()
    formErrors = graphene.String()
    client = graphene.Field(ClientType)

    @staticmethod
    def mutate(root, info, context, clientName, clientPhone, clientAddress):
        if not context.user.is_authenticated():
            return CreateMessageMutation(status=403)

        # Here we would usually use Django forms to validate the input
        if not clientName:
            return CreateMessageMutation(
                status=400,
                formErrors=json.dumps(
                    {
                        'clientName': ['Please enter Client name'], 
                        'clientAddress': ['Please enter Client address'],
                        'clientPhone': ['Please enter Client phone']}))

        obj = models.Client.objects.create(
            clientName=clientName, clientAddress=clientAddress, clientPhone=clientPhone
        )

        return CreateMessageMutation(status=200, message=obj)


class Mutation(graphene.AbstractType):
    create_client = CreateMessageMutation.Field()