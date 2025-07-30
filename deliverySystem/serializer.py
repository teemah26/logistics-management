from rest_framework import serializers
from deliverySystem.models import Vehicle
from deliverySystem.models import VehicleCategory
from deliverySystem.models import Driver
from deliverySystem.models import DeliveryMission
import deliverySystem.views
from django.contrib.auth.models import User

class VehicleCategorySerializer(serializers.HyperlinkedModelSerializer):
    deliverySystem = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='vehicle-detail'
    )
    class Meta:
        model=VehicleCategory
        fields=(
            'url',
            'pk',
            'name',
            'deliverySystem'
        )

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_category=serializers.SlugRelatedField(queryset=VehicleCategory.objects.all(),slug_field='name')
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Vehicle
        fields=(
            'url',
            'name',
            'owner',
            'vehicle_category',
            'added_date',
            'license_number',
            'in_use',
          
        )
class DeliveryMissionSerializer(serializers.HyperlinkedModelSerializer):
    vehicle =VehicleSerializer()
    class Meta:
        model = DeliveryMission
        fields=(
            'url',
            'pk',
            'destination',
            'distance_km',
            'vehicle',
            'delivery_date',
            'driver'
        )        

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    DeliveryMissions=DeliveryMissionSerializer(many=True,read_only=True)
    gender=serializers.ChoiceField(
        choices=Driver.GENDER_CHOICES)
    gender_description=serializers.CharField(source='get_gender_display',read_only=True)
    class Meta:
        model =Driver
        fields=(
            'url',
            'name',
            'gender',
            'gender_description',
            'mission_completed',
            'hired_on',
            'DeliveryMissions'
            
        )
class DeliveryMissionSerializer(serializers.ModelSerializer):
    
    vehicle=VehicleSerializer()
    class Meta:
        model = DeliveryMission
        fields=(
            'url',
            'pk',
            'distance_km',
            'delivery_date',
            'vehicle'
        )        
  
        
class DriverDeliveryMissionSerializer(serializers.ModelSerializer):
    driver=serializers.SlugRelatedField(queryset=Driver.objects.all(),slug_field='name')
    vehicle=serializers.SlugRelatedField(queryset=Vehicle.objects.all(),slug_field='name')
    class Meta:
        model=DeliveryMission
        fields=(
            'url',
            'pk',
            'distance_km',
            'driver',
            'vehicle',
            
        )

class UserVehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Vehicle
        fields=(
             'url',
            'name'
            )
class UserSerializer(serializers.HyperlinkedModelSerializer):
    deliverySystem=UserVehicleSerializer(
        many=True,
        read_only=True
    ) 
    class Meta:
        model=User
        fields=(
            'url',
            'pk',
            'username',
            'vehicle'
        )           