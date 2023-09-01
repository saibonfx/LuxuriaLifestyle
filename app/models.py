from django.db import models

class ServiceRequest(models.Model):
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    # Other fields as needed


class JobRequest(models.Model):
    pickup_location = models.CharField(max_length=100)  # Define the pickup_location field
    destination = models.CharField(max_length=100) 
    date = models.DateField()
    time = models.TimeField()
    driver_accepted = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # Other fields as needed
    
    objects = models.Manager()  # Add this line to define the 'objects' manager
