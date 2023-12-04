from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    number_available = models.IntegerField()
    total_capital = models.GeneratedField()