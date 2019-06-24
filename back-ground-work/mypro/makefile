init : users paper


start:
	django-admin startproject mypro

app:
	python3 manage.py startapp myapp
run:
	python3 manage.py runserver 0.0.0.0:8080
testrun:
	python3 manage.py runserver 8080
key:
	python3 myapp/views.getkey
test: test_users
	@pwd
test_users:
	python3 manage.py test users

users:
	python3 manage.py startapp users
paper:
	python3 manage.py startapp paper

models:
	python3 manage.py makemigrations users
	python3 manage.py migrate