from django.db import models

from django.utils import timezone
# Create your models here.

class Article(models.Model):
	link 		= models.CharField(max_length=100)
	source 		= models.CharField(max_length=100, blank=True, default='')
	thumbnail 	= models.CharField(max_length=100, blank=True, default='')
	view_count 	= models.IntegerField(default=0)
	snippet		= models.CharField(max_length=100, blank=True, default='')
	title		= models.CharField(max_length=100)
	fetched_on  = models.DateTimeField(default=timezone.now())

	def __str__():
		print 'Title:', title, '\nLink:', link
