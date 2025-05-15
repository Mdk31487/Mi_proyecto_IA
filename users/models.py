# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)  # Campo extra opcional

def __str__(self):
    return f'Perfil de {self.user.username}'
