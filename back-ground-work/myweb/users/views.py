from django.shortcuts import render
from django.http import HttpResponse
from .models import user

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
# 	user_list = user.objects.order_by('username')
# 	output = ", ".join([u.username for u in user_list])
# 	return HttpResponse(output)

def index(request):
	return render(request, 'users/index.html')

def login(request):
	try:
		user.get(pk = request.POST['account'])
	except(KeyError, user.username):
		return HttpResponse("there is no username as "+request.POST['account'] )
	