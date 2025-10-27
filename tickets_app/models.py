from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth =  models.DateField(blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username