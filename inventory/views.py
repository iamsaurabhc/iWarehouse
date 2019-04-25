from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Client


def index(request):
    try:
        clients = Client.objects.order_by('-clientAddress')[:5]
        context = {'clients': clients, }
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'inventory/index.html', context)


def detail(request, clientID):
    return HttpResponse("You're looking at Client %s." % clientID)
