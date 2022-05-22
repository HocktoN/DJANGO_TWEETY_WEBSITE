import email
from django.db import models
from django.contrib.auth.models import User


class Gonderi(models.Model):

    icerik = models.CharField(max_length=50)
    image = models.ImageField(blank=True,null = True)
    date = models.DateTimeField(auto_now=True,null=True)
    kullanici = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.icerik[:10] +"..."

# Create your models here.
