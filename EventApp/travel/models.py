from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class TravelModel(models.Model):
    title= models.CharField(verbose_name="Başlık", max_length=255)
    content= HTMLField()
    thumbnail_image=models.ImageField(verbose_name='Kapak Fotoğrafı',upload_to='events/')
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    c_date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


