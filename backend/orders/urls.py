from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('client/', views.get_client_orders, name='get_client_orders'),
]