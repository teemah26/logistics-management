from django.db import models

# Create your models here.
class VehicleCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, default="",unique=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    name = models.CharField(max_length=100, blank=False, default="")
    category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100, blank=False, default="", unique=True)
    added_date = models.DateTimeField(auto_now_add=True)
    in_use = models.BooleanField(default=True)

    class Meta:
        ordering = ('license_number',)

    def __str__(self):
        return f"{self.vehicle_number} - {self.category.name}"
    
class Driver(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
    (MALE,'Male'),
    (FEMALE,'Female'),
    )
    name = models.CharField(max_length=100, blank=False, default="")
    mission_completed = models.IntegerField(default=0)
    gender= models.CharField(max_length=2,choices=GENDER_CHOICES,default=MALE)
    hired_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class DeliveryMission(models.Model):    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255, blank=False, default="")
    distance_km = models.FloatField(default=0.0)  # Distance in kilometers
    delivery_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('destination',)

    def __str__(self):
        return f"Mission {self.id} by {self.driver.name} using {self.vehicle.name}"