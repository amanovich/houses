from django.urls import path
from . import views


urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('home/', views.home_view, name='home'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('booking/', views.booking_request, name='booking_request'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.property_create, name='property_create'),
    path('api/properties/<int:pk>/',PropertyDetailAPIView.as_view(), name='api_property_detail'),
]

