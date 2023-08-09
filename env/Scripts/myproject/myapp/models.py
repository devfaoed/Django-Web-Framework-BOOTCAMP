from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink = models.CharField(max_length = 200)
    price = models.IntegerField()


class userinfo(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length= 200)
    age = models.IntegerField()
    comment = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
