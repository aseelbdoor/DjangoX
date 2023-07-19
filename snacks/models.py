from django.db import models
from accounts.models import CustomUser
from django.urls import reverse_lazy, reverse

# Create your models here.
class Snack(models.Model):
    title=models.CharField(max_length=200,help_text='Title')
    purchaser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description=models.TextField(default="No description")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("List")