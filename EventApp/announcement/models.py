from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class AnnouncementModel(models.Model):
    title= models.CharField(verbose_name="Başlık", max_length=255)
    content=HTMLField()
    c_date=models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title