from django.shortcuts import render, get_object_or_404, redirect
from .models import House, Location, Feature
from .forms import BookingRequestForm
from rest_framework import viewsets
from .serializers import PropertySerializer
from .forms import PropertyForm
from .models import  Region
from .forms import HouseRequestForm
from .forms import RequestFormForm
from django.contrib import messages
from rest_framework.generics import RetrieveAPIView
from .models import Property



class PropertyDetailAPIView(RetrieveAPIView):
    queryset = Property.objects.all()
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
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

# def property_create(request):
#     if request.method == 'POST':
#         form = PropertyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('property_list')
#     else:
#         form = PropertyForm()
#     return render(request, 'property_form.html', {'form': form})


def property_list(request):
    region_id = request.GET.get('region')  # получаем id из GET-запроса
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



def home(request):
    if request.method == 'POST':
        form = HouseRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Сделай отдельную страницу "Спасибо"
    else:
        form = HouseRequestForm()
    return render(request, 'home.html', {'form': form})


def home_view(request):
    if request.method == 'POST':
        form = RequestFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Название маршрута
    else:
        form = RequestFormForm()
    return render(request, 'home.html', {'form': form})




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



