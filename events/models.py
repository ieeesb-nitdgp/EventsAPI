from django.db import models
from django import forms
import datetime


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.ImageField(upload_to='media/img',blank=True, default="media/img/transparent.jpg")
    image_1 = models.ImageField(upload_to='media/img',blank=True, default='media/img/transparent.jpg')
    image_2 = models.ImageField(upload_to='media/img',blank=True, default='media/img/transparent.jpg')
    image_3 = models.ImageField(upload_to='media/img',blank=True, default='media/img/transparent.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    event_date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title