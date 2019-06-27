from django.db import models
from users.models import User
# Create your models here.
class Paper(models.Model):
	title = models.CharField(max_length=128)
	select_question_num = models.IntegerField(default=0)
	fill_question_num = models.IntegerField(default=0)
	creater = models.CharField(max_length=128)

class Question_select(models.Model):
	paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	option_num = models.IntegerField(default=0)
	mytype = models.CharField(max_length=128)

class Option(models.Model):
	question = models.ForeignKey(Question_select, on_delete=models.CASCADE)
	text = models.CharField(max_length=128)
	vote_num = models.IntegerField(default=0)

class Question_fill(models.Model):
	paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)

class Question_fill_answer(models.Model):
	question = models.ForeignKey(Question_fill, on_delete=models.CASCADE)
	answer = models.CharField(max_length=128)
	author = models.CharField(max_length=128,default='null')

class Option_vote(models.Model):
	option = models.ForeignKey(Option, on_delete=models.CASCADE)
	voter = models.CharField(max_length=128, default='null')