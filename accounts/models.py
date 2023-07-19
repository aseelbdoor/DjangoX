from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phoneNumber=models.CharField(max_length=12,blank=True,null=True)

    def __str__(self):
        return self.username