from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class Teammates(models.Model):
    heading=models.CharField(max_length=250)
    picture=models.ImageField(upload_to='pics')
    details=models.TextField()
    def __str__(self):
        return self.heading