from django.db import models

# Create your models here.

class User(models.Model):
	nickname = models.CharField(max_length = 20)
	studentid = models.IntegerField(default = 0)
	age = models.IntegerField(default = 0)
	sex = models.IntegerField(default = 0)
	# 0 = default, 1 = male, 2 = female
	grade = models.CharField(max_length = 20)
	major = models.CharField(max_length = 20)
	image = models.CharField(max_length = 20)
	email = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	phone = models.CharField(max_length = 20)
	userStatus = models.IntegerField(default = 0)

class Paper(models.Model):
	creator = models.ForeignKey(User)
	title = models.CharField(max_length = 20)
	detail = models.CharField(max_length = 200)
	state = models.IntegerField(default = 0)



class Question(models.Model):
	paper = ForeignKey(Paper, on_delete=models.CASCADE)
	q_type = models.IntegerField(default = 0)
	# 问题类型  1 单选  2 多选 3 问答
	content = models.CharField(max_length = 200)

class Choice(models.Model):
	choice_text = models.CharField(max_length = 20)
	question = ForeignKey(Question, on_delete=models.CASCADE)
	votes = models.IntegerField(default = 0)

class Submit(models.Model):
	user = ForeignKey(User, on_delete=models.CASCADE)
	paper = ForeignKey(Paper, on_delete=models.CASCADE)
	question = ForeignKey(Question, on_delete=models.CASCADE)
	choice = ForeignKey(Choice, on_delete=models.CASCADE)
		





# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)