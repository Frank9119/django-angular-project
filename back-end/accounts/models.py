from django.db import models
from django.contrib.auth.models import AbstractUser

from mixin.models import BaseModel
from django.conf import settings


# Create your models here.
USER_ROLES = (
    ('ADMIN', 'ADMIN'),
    ('NORMAL_USER', 'NORMAL_USER'),

)

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),

)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default="NORMAL_USER")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['email']


class Profile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, unique=True)
    addres = models.CharField(max_length=10)


    def __str__(self):
        return f"{self.user} 's Profile"
    
    class Meta:
        verbose_name = 'User_profile'
        verbose_name_plural = 'User_profiles'
        ordering = ['-primary_key']
