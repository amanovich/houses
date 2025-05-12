from django.urls import path
from . import views


urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('booking/', views.booking_request, name='booking_request'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.property_create, name='property_create'),
]
