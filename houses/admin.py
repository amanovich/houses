from django.contrib import admin
from .models import (
    Property, Feature, Region, District, Location,
    House, HouseImage, Hostel, PropertyImage,
    Apartment, Hotel  # прокси-модели
)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'street', 'house_number', 'apartment_number', 'phone_number']
    list_filter = ['type', 'district__region']
    search_fields = ['street', 'house_number', 'apartment_number']


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'street', 'house_number', 'apartment_number', 'phone_number', 'district']
    search_fields = ['street', 'house_number']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(type='apartment')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'street', 'house_number', 'apartment_number', 'phone_number', 'district']
    search_fields = ['street', 'house_number']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(type='hotel')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']
    list_filter = ['region']
    search_fields = ['name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'location', 'price_per_day', 'beds']
    search_fields = ['title', 'location']


@admin.register(HouseImage)
class HouseImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'house', 'image']


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'price_per_night']
    search_fields = ['name']


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'property', 'image']
