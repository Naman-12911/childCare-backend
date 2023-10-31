from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils.translation import gettext_lazy  as _
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
from django.contrib.auth.models import User


# resgiter the user
AUTH_PROVIDERS = {'email': 'email'}
class User(AbstractUser):
    phone_no = models.CharField(unique=True,  null=True,max_length=10)
    Facility_Administrator = models.BooleanField(default=False)
    teacher = models.BooleanField(default=False)
    parent = models.BooleanField(default=False)
    name = models.CharField(max_length=100,null=True)
    
    REQUIRED_FIELDS = []
  