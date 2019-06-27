init : users paper mission


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

test:
	python3 manage.py test users
	python3 manage.py test paper
test_users:
	python3 manage.py test users
test_papers:
	python3 manage.py test paper

	
users:
	python3 manage.py startapp users
paper:
	python3 manage.py startapp paper
mission:
	python3 manage.py startapp mission

models:
	python3 manage.py makemigrations users
	python3 manage.py makemigrations paper
	python3 manage.py migrate