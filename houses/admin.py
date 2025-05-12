from django.contrib import admin
from .models import House, Location, Feature
from .models import HouseImage, BookingRequest
from .models import Region, District, Property
admin.site.register(House)
admin.site.register(Location)
admin.site.register(Feature)
admin.site.register(HouseImage)
admin.site.register(BookingRequest)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Property)
