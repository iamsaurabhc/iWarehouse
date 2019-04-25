from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /inventory/5/
    path('<int:clientID>/', views.detail, name='detail'),
]