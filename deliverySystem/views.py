from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from deliverySystem.models import Vehicle
from deliverySystem.models import VehicleCategory
from deliverySystem.models import Driver
from deliverySystem.models import DeliveryMission
from deliverySystem.serializer import VehicleCategorySerializer 
from deliverySystem.serializer import VehicleSerializer 
from deliverySystem.serializer import DriverSerializer
from deliverySystem.serializer import DeliveryMissionSerializer
import django_filters
from django_filters import AllValuesFilter,DateTimeFilter,NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import AllValuesFilter,DateTimeFilter,NumberFilter
from rest_framework import filters
from rest_framework import permissions
from deliverySystem import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication







class VehicleCategoryList(generics.ListCreateAPIView):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer
    name = 'vehiclecategory-list'
    filter_fields = (
        'name',
    )
    search_fields = (
        '^name'
    )
    ordering_fields = (
        'name',
    )

class VehicleCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer
    name = 'vehiclecategory-detail' 

class VehicleList(generics.ListCreateAPIView):
    throttle_scope ='user'
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-list'
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields = [
        'name',
        'vehicle_category',
        'added_date',
        'license_number',
        'in_use'
    ]
    search_fields = [
        '^name'
    ]
    ordering_fields = [
        'name',
        'added_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOrReadOnly,
    )

   
class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope ='anon'
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-detail'
class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    throttle_scope ='anon'
    serializer_class = DriverSerializer
    name = 'driver-list'
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filter_fields = [
        'name',
        'gender',
        'mission_completed',
    ]
    search_fields = [
        '^name'
    ]
    ordering_fields = [
        'name',
        'mission_completed',]
    authentication_classes = (TokenAuthentication,
                              )
    permission_classes=(
        IsAuthenticated
    )
class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope ='anon'
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    name = 'driver-detail'
    authentication_classes = (TokenAuthentication,
                              )
    permission_classes=(
        IsAuthenticated
    )



class DeliveryMissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryMission.objects.all()
    serializer_class = DriverSerializer
    name = 'deliveryMission-detail'
class DeliveryMissionFilter(django_filters.FilterSet):
    driver = AllValuesFilter(field_name='driver__name')
    vehicle = AllValuesFilter(field_name='vehicle__name')
    distance_km = NumberFilter(field_name='distance_km', lookup_expr='exact')
    delivery_date = DateTimeFilter(field_name='distance_acheivement_date', lookup_expr='gte')
   
    class Meta:
        model = DeliveryMission
        fields = ['driver', 'vehicle', 'distance_km', 'delivery_date',] 
class DeliveryMissionList(generics.ListCreateAPIView):
    queryset = DeliveryMission.objects.all()
    serializer_class = DriverSerializer
    name = 'deliveryMission-list'
    filter_class = DeliveryMissionFilter
    ordering_fields = (
        'distance_km',
        'delivery_date',
    )
class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'vehicle-categiries': reverse(VehicleCategoryList.name, request=request),
            'drones': reverse(VehicleList.name, request=request),
            'pilots': reverse(DriverList.name, request=request),
            'competitions': reverse(DeliveryMissionList.name, request=request),
        })

