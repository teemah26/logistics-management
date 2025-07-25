from django.urls import path, include
from deliverySystem import views

urlpatterns=[
    path('vehicle-categories/',views.VehicleCategoryList.as_view(),name=views.VehicleCategoryList.name),
    path('vehicle-categories/<int:pk>',views.VehicleCategoryDetail.as_view(),name=views.VehicleCategoryDetail.name),
    path('vechicle/',views.VehicleList.as_view(),name=views.VehicleList.name),
    path('vechile/<int:pk>',views.VehicleDetail.as_view(),name=views.VehicleDetail.name),
    path('driver/',views.DriverList.as_view(),name=views.DriverList.name),
    path('driver/<int:pk>',views.DriverDetail.as_view(),name=views.DriverDetail.name),
    path('delivery-mission/',views.DeliveryMissionList.as_view(),name=views.DeliveryMissionList.name),
    path('delivery-mission/<int:pk>',views.DeliveryMissionDetail.as_view(),name=views.DeliveryMissionDetail.name),
    path('',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]