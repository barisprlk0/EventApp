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


    def avarage_rating(self):
        ratings=self.ratings.all()
        if ratings.exists():
            return sum(rating.value for rating in ratings) / ratings.count()
        return 0
    
class Rating(models.Model):
    travel_post= models.ForeignKey(TravelModel,related_name='ratings',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    value=models.PositiveSmallIntegerField(default=1, choices=[(i,i) for i in range(1,6)])
    class Meta: 
        unique_together=('travel_post','user')