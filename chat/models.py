from django.db import models

# Create your models here.

class Destination(models.Model):
    username = models.CharField(max_length=100)
    balance = models.IntegerField()

class log(models.Model):
    username=models.CharField(max_length=100)
    Transaction_Type = models.CharField(max_length=100)
    amount = models.IntegerField()