from django.db import models
from django import forms
import datetime

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

 
    def __str__(self):
        return self.name
