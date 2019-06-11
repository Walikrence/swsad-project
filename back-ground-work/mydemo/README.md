# 环境要求



```
# Django 版本2.1.7 而且是 python3
pip install Django==2.1.7
# 这个也要安装
pip install django-cors-headers
#运行
python manage.py runserver 8000

```





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
model范例
```py
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

激活模型
```sh
python3 manage.py makemigrations users
python3 manage.py migrate
```

---
[登陆注册参考资料](https://www.cnblogs.com/derek1184405959/p/8567522.html)
[django上传图片并使用](https://blog.csdn.net/boycycyzero/article/details/43820481)