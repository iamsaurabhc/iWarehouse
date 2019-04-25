from django.contrib import admin

# Register your models here.
from .models import Client, Product, Edge, Node, Pallet, ProductBundle

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(ProductBundle)
admin.site.register(Edge)
admin.site.register(Node)
admin.site.register(Pallet)