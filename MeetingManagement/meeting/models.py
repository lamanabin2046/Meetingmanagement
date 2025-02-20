from django.db import models

# Create your models here.

from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
import json

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'ADMIN'),
        (2, 'CAO'),
        (3, 'ACCOUNTANT'),
        (4, 'ENGINEER'),
        (5, 'SUBENGINEER'),
        (6, 'PLANNINGOFFICER'),
        (7, 'WARDSACHIB'),

    )
   
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    