# from django.contrib import admin
# from django.urls import include, path

from django.urls import path

from . import views

urlpatterns = [
    path('users/signin', views.index, name='index'),
]