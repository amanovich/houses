from rest_framework import serializers
from .models import Property, House

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
