from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="form")
    

class Car(models.Model):
    Car_name = models.CharField(max_length=300)
    Car_description = models.TextField(max_length=1000)
    Car_image  = models.ImageField(upload_to="Car")
    