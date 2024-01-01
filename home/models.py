from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    car_name =  models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

class Post(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/', default='default_image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
