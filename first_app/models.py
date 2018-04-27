from __future__ import unicode_literals
from django.conf import settings
from django.db import models



class Topic(models.Model):
	top_name= models.CharField(max_length=264, unique=True)


	def __str__(self):
		return self.top_name

class WebPage(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
	date = models.DateField()
	

	def __str__(self):
		return str(self.date)


class RollStock(models.Model):
	width = models.IntegerField()
	paperType = models.CharField(max_length=264, unique=True)
	lineal = models.IntegerField()
	weight = models.DecimalField(decimal_places=3, max_digits=10)
	quantity = models.DecimalField(decimal_places=3, max_digits=10)

	def __str__(self):
		return str(self.quantity, self.paperType)



class User(models.Model):
	firstname = models.CharField(max_length=264, unique=True)
	lastname = models.CharField(max_length=264, unique=True)
	email = models.CharField(max_length=264, unique = True)

	def __str__(self):
		return str(self.email)

class Coordinates(models.Model):
	#id = models.IntegerField(primary_key=True)
	latitude = models.DecimalField(decimal_places=10, max_digits=16)
	longitude = models.DecimalField(decimal_places=10, max_digits=16)
	altitude = models.DecimalField(decimal_places=10, max_digits=16)
	intensity = models.DecimalField(decimal_places=10, max_digits=16)

	def __str__(self):
		return str(self.latitude, self.longitude)
	#user, firstname, lastname, email
	#populate fake user, create view, html, list of names
	#template tags

from django.db import models
from geoposition.fields import GeopositionField

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()



# Create your models here.
