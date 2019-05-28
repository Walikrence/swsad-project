from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class User(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	avatar = models.ImageField(upload_to='avatar', default='image.jpg')
	#---
	nickname = models.CharField(max_length = 20, default = 'not filled')
	studentid = models.IntegerField(default = 0)
	age = models.IntegerField(default = 0)
	sex = models.IntegerField(default = 0)
	grade = models.CharField(max_length = 20, default = 'not filled')
	major = models.CharField(max_length = 20, default = 'not filled')
	email = models.CharField(max_length = 20, default = 'not filled')
	phone = models.CharField(max_length = 20, default = 'not filled')
	create_date = models.DateTimeField('创建日期', auto_now_add = True)

class Paper(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length = 20, default = 'not filled')
	detail = models.CharField(max_length = 200, default = 'not filled')
	state = models.IntegerField(default = 0)
	create_date = models.DateTimeField('创建日期', auto_now_add = True)



class Question(models.Model):
	paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
	q_type = models.IntegerField(default = 0)
	# 问题类型  1 单选  2 多选 3 问答
	content = models.CharField(max_length = 200, default = 'not filled')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length = 20, default = 'not filled')
	votes = models.IntegerField(default = 0)

class Submit(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
	create_date = models.DateTimeField('创建日期', auto_now_add = True)
		





# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)