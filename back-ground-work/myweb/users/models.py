from django.db import models

class user(models.Model):
	"""docstring for username"""
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	def __str__(self):
		return self.username

# Create your models here.
