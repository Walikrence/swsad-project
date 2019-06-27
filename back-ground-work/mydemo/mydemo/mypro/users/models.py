from django.db import models
# Create your models here.
class User(models.Model):

	gender = (
	    ('male', '男'),
	    ('female', '女')
	)

	name = models.CharField(max_length=128, unique=True)
	password = models.CharField(max_length=256, default='123456')
	email = models.EmailField(default='asd@asd')
	sex = models.CharField(max_length=32, choices=gender, default='男')

	def __str__(self):
		return self.name