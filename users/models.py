from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True )
    name = models.CharField(max_length=255, null=True, blank=True)
    
    
    
    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    
