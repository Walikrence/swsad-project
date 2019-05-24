from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.


@csrf_exempt
def signin(request):
    resp = {'myname': 'walikrence', 'passwd': '123456'}
    return HttpResponse(json.dumps(resp), content_type="application/json")