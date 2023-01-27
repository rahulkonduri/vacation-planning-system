from django.db import models

class Destination(models.Model):
    # id: int
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
# Create your models here.
