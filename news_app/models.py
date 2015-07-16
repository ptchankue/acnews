from django.db import models

# Create your models here.

class Article(models.Model):
	link 		= models.CharField(max_length=100)
	source 		= models.CharField(max_length=100)
	thumbnail 	= models.CharField(max_length=100)
	view_count 	= models.IntegerField()
	snippet		= models.CharField(max_length=100)
	title		= models.CharField(max_length=100)