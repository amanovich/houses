from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, HouseViewSet, ApartmentViewSet, HotelViewSet, HostelViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')
router.register(r'houses', HouseViewSet, basename='house')
router.register(r'apartments', ApartmentViewSet, basename='apartment')
router.register(r'hotels', HotelViewSet, basename='hotel')
router.register(r'hostels', HostelViewSet, basename='hostel')

urlpatterns = router.urls
