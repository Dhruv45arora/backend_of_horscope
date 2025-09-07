from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    birth_time = models.TimeField(null=True, blank=True)
    
