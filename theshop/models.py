from shop.models import Product
from django.db import models

class AcrylicPainting(Product):
	picture = models.ImageField(upload_to='img/acrylic')
	medium = models.CharField(max_length=30, default=0)
	height = models.IntegerField(default=0)
	width = models.IntegerField(default=0)
	short_description = models.CharField(max_length=255, default=0)
	long_description = models.TextField(blank=True, null=True)

	class Meta:
		ordering = ['date_added']

class OilPainting(Product):
	picture = models.ImageField(upload_to='img/oil')
	medium = models.CharField(max_length=30, default=0)
	height = models.IntegerField(default=0)
	width = models.IntegerField(default=0)
	short_description = models.CharField(max_length=255, default=0)
	long_description = models.TextField(blank=True, null=True)

	class Meta:
		ordering = ['date_added']

class PencilSketch(Product):
	picture = models.ImageField(upload_to='img/pencil')
	medium = models.CharField(max_length=30, default=0)
	height = models.IntegerField(default=0)
	width = models.IntegerField(default=0)
	short_description = models.CharField(max_length=255, default=0)
	long_description = models.TextField(blank=True, null=True)

	class Meta:
		ordering = ['date_added']
		verbose_name_plural = 'pencil sketches'
	
class PastelDrawing(Product):
	picture = models.ImageField(upload_to='img/pastel')
	medium = models.CharField(max_length=30, default=0)
	height = models.IntegerField(default=0)
	width = models.IntegerField(default=0)
	short_description = models.CharField(max_length=255, default=0)
	long_description = models.TextField(blank=True, null=True)

	class Meta:
		ordering = ['date_added']
