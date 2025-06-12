from rest_framework import serializers
from .models import House, Hostel
from .models import Property, Feature



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

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'  # или перечисли: ['name', 'location', 'price_per_night', ...]

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']

class PropertySerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)
    feature_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Feature.objects.all(),
        write_only=True,
        source='features'
    )
    region_name = serializers.CharField(source='district.region.name', read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'type', 'custom_id',
            'street', 'house_number', 'apartment_number',
            'phone_number', 'district', 'region_name', 'district_name',
            'features', 'feature_ids'
        ]
