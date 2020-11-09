from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Origin(models.Model):
	superhero=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
	origin=models.CharField(max_length=200,unique=True)
class Location(models.Model):
	latitud=models.FloatField(unique=True)
	longitude=models.FloatField(unique=True)
	country=models.CharField(max_length=200)
class Sighting(models.Model):
	superhero=models.ForeignKey(User,on_delete=models.CASCADE)
	power=models.CharField(max_length=200)
	location=models.ForeignKey(Location,on_delete=models.CASCADE)
	sighted_on=models.DateTimeField()