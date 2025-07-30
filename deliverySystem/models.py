from django.db import models

# Create your models here.
class VehicleCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, default="",unique=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    name = models.CharField(max_length=250,unique=True)
    vehicle_category = models.ForeignKey(VehicleCategory, related_name='deliverySystem',on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100, unique=True)
    added_date = models.DateTimeField(auto_now_add=True)
    in_use = models.BooleanField(default=True)

    owner = models.ForeignKey(
           'auth.User',
           null=True,
           related_name='deliverySystem',
           on_delete=models.CASCADE
    )
        
    class Meta:
            ordering = ('name',)
    def __str__(self):
            return self.name
    
class Driver(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
    (MALE,'Male'),
    (FEMALE,'Female'),
    )
    name = models.CharField(max_length=100, blank=False, default='',unique=True)
    mission_completed = models.IntegerField()
    gender= models.CharField(max_length=2,choices=GENDER_CHOICES,default=MALE)
    hired_on = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
           'auth.User',
           null=True,
           related_name='drivers',
           on_delete=models.CASCADE
    )

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

