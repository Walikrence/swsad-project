# 快速开始
~~~sh
python3 manage.py runserver 8000
~~~

# 访问
浏览器访问

[网站](127.0.0.1:8000)

---

启动项目
```sh
django-admin startproject mysite
```
启动应用
```sh
python3 manage.py startapp users
```

url.py范例
```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
view.py范例
```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
返回json范例
```py
import json
from django.http import HttpResponse


def get_an_apple(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
```

主url.py范例
```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
````

解决CSRF token missing or incorrect.
```py
from django.views.decorators.csrf import csrf_exempt 
@csrf_exempt
def some_view(request):
    #...
```