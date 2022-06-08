from django.db import models

# Create your models here.
class Book(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.FloatField()
    Author = models.CharField(max_length=100)
    Release_date = models.DateField()

