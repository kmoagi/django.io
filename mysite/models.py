from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models


class CustomUser(AbstractUser):
    home_address = models.CharField(max_length=255, blank=True) #CharField that allows up to 225 characters
    phone_number = models.CharField(max_length=20, blank=True)  #CharField that allows up to 20 characters
    location = models.PointField(null=True, blank=True)  #PointField, which represents a point geometry for the user's location. The null=True and blank=True parameters allow the field to be optional.

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.user.username    