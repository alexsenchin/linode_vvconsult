from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('services/', views.services_long_decription, name='services_long_decription'),
    path('contacts/', views.contacts, name='contacts')
]
