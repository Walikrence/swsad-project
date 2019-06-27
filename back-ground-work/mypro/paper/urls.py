from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	# path('index/',views.index),
	path('create/',views.create),
	path('delete/',views.delete),
	path('query/',views.query),
	path('fill/',views.fill),

]
