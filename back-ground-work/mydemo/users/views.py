from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from django.db import models
from .models import User
# Create your views here.


@csrf_exempt
def signin(request):
	if request.method == 'POST':
		print (request.session.get('is_login',None))
		request.session['is_login'] = True
		print (request.session.get('is_login',None))

		received_json_data = json.loads(request.body)
		username = received_json_data.get('account')
		password = received_json_data.get('password')
		if username and password:
			# 用户名字符合法性验证
			# 密码长度验证
			# 更多的其它验证.....
			try:
				user = User.objects.get(username = username)
			except:
				resp = {'status': 'fail'}
				return HttpResponse(json.dumps(resp), content_type="application/json")
			if user.password == password:
				resp = {'status': 'success'}
				return HttpResponse(json.dumps(resp), content_type="application/json")
			resp = {'status': 'fail'}
			return HttpResponse(json.dumps(resp), content_type="application/json")



# if username and password:  # 确保用户名和密码都不为空
#             username = username.strip()
#             # 用户名字符合法性验证
#             # 密码长度验证
#             # 更多的其它验证.....
#             try:
#                 user = models.User.objects.get(name=username)
#             except:
#                 return render(request, 'login/login.html')
#             if user.password == password:
#                 return redirect('/index/')
#     return render(request, 'login/login.html')