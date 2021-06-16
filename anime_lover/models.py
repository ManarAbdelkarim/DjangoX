from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete= CASCADE)
    image = models.ImageField(upload_to='static/images', null = True)
    description = models.TextField(default='an awesome anime series')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('anime_detail',args=[str(self.id)])