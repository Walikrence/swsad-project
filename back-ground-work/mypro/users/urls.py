from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin),
    path('register/', views.register),
]
