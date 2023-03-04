from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class User(AbstractUser):
    is_salaries = models.BooleanField(default=False)
    is_RH_Campagnies = models.BooleanField(default=False)
    is_admin_WebApps = models.BooleanField(default=True)