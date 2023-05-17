from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    home_address = models.CharField(max_length=255, blank=True) #CharField that allows up to 225 characters
    phone_number = models.CharField(max_length=20, blank=True)  #CharField that allows up to 20 characters