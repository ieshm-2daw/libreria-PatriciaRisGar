from django.contrib.auth.models import AbstractServer
from django.db import models

# Create your models here.

class User(AbstractServer):
    dni = models.CharField(max_length='9')
    adress = models.CharField()
    telefono = models.PhoneNumberField()
    

