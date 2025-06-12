from django.shortcuts import render, get_object_or_404, redirect
from .models import House, Location, Feature, Property, Region
from .forms import BookingRequestForm, PropertyForm, HouseRequestForm, RequestFormForm
from django.contrib import messages
from rest_framework import viewsets, generics
from .serializers import PropertySerializer, HouseSerializer
from .models import BookingRequest
from django.contrib.auth.decorators import login_required

@login_required
def confirm_booking(request, pk):
    booking = get_object_or_404(BookingRequest, pk=pk)
    booking.is_confirmed = True
    booking.save()
    messages.success(request, "Бронирование подтверждено.")
    return redirect('booking_list')


def booking_list(request):
    bookings = BookingRequest.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class ApartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.filter(type='apartment')
    serializer_class = PropertySerializer


class HouseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.filter(type='house')
    serializer_class = PropertySerializer


class HotelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.filter(type='hotel')
    serializer_class = PropertySerializer


class HostelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.filter(type='hostel')
    serializer_class = PropertySerializer


def house_list(request):
    houses = House.objects.all()
    return render(request, 'houses/house_list.html', {'houses': houses})


def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'houses/house_detail.html', {'house': house})


def booking_request(request):
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('house_list')
    else:
        form = BookingRequestForm()
    return render(request, 'houses/booking_form.html', {'form': form})


def property_list(request):
    region_id = request.GET.get('region')
    properties = Property.objects.all()
    regions = Region.objects.all()

    if region_id:
        properties = properties.filter(region_id=region_id)

    return render(request, 'property_list.html', {
        'properties': properties,
        'regions': regions,
        'selected_region': int(region_id) if region_id else None
    })


def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.region = property_obj.district.region  # автоустановка региона
            property_obj.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.filter(type='apartment')
    serializer_class = PropertySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.filter(type='hotel')
    serializer_class = PropertySerializer


class HostelViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.filter(type='hostel')
    serializer_class = PropertySerializer


def home_view(request):
    if request.method == 'POST':
        form = RequestFormForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, заявка принята!')
            return redirect('home')
    else:
        form = RequestFormForm()
    return render(request, 'home.html', {'form': form})




