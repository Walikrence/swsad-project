from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User


# Create your views here.

@csrf_exempt
def signin(request):
	message = '您已登录，请不要重复登录'
	if request.session.get('is_signin'):  # 不允许重复登录
		resp = {'message': message,'code' : 0}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	if request.method == 'POST':
		received_json_data = json.loads(request.body)
		name = received_json_data.get('username')
		password = received_json_data.get('password')
		try:
			user = User.objects.get(name=name)
		except:

			message = '该用户不存在'
			resp = {'message': message, 'code':1}
			return HttpResponse(json.dumps(resp), content_type="application/json")
		else:
			if user.password == password:
				request.session['is_signin'] = True
				request.session['user_id'] = user.id
				request.session['user_name'] = user.name

				message = '登录成功'
				email = user.email
				sex = user.sex
				name = user.name

				resp = {
				'message': message,
				'code': 2,
				'sex': sex,
				'email':email,
				'name':name
				}

				return HttpResponse(json.dumps(resp), content_type="application/json")
			else:
				message = '密码错误'
				resp = {'message': message, 'code':3}
				return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		return HttpResponse("Hello, world. You're at the signin.")		

@csrf_exempt
def register(request):
	message = '您已登录，请不要重复登录'
	if request.session.get('is_signin'):  # 不允许重复登录
		resp = {'message': message,'code' : 0}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	if request.method == 'POST':
		received_json_data = json.loads(request.body)
		name = received_json_data.get('username')
		password = received_json_data.get('password')
		email = received_json_data.get('email')
		try:
			user = User.objects.get(name = name)
		except:
			message = '注册成功' 
			u = User(name = name, password = password, email = email)
			u.save()
			resp = {'message': message,'code' : 2}
			return HttpResponse(json.dumps(resp), content_type="application/json")
		else:
			message = '用户名已经存在'
			resp = {'message': message,'code' : 1}
			return HttpResponse(json.dumps(resp), content_type="application/json")
	return HttpResponse("Hello, world. You're at the register.")

