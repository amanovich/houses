from django.urls import path
from . import views
from .views import (
    ApartmentDetailAPIView,
    HouseDetailAPIView,
    HotelDetailAPIView,
    HostelDetailAPIView,
    PropertyDetailAPIView,
)
from .views import confirm_booking
from .views import booking_list
from .views import property_list

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('home/', views.home_view, name='home'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('booking/', views.booking_request, name='booking_request'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.property_create, name='property_create'),
    path('api/apartments/<int:pk>/', ApartmentDetailAPIView.as_view(), name='api_apartment_detail'),
    path('api/houses/<int:pk>/', HouseDetailAPIView.as_view(), name='api_house_detail'),
    path('api/hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='api_hotel_detail'),
    path('api/hostels/<int:pk>/', HostelDetailAPIView.as_view(), name='api_hostel_detail'),
    path('api/properties/<int:pk>/', PropertyDetailAPIView.as_view(), name='api_property_detail'),
    path('booking-confirm/<int:pk>/', confirm_booking, name='confirm_booking'),
    path('booking-requests/', booking_list, name='booking_list'),
    path('bookingrequest/<int:pk>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('properties/', property_list, name='property_list'),
]
