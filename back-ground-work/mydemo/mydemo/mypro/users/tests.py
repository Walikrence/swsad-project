from django.test import TestCase
from .models import User
from django.test import Client
from django.test.utils import setup_test_environment
import json


class TEST_USER(TestCase):
	def setUp(self):
		u = User(name='walikrence', password="123456")
		u.save()
	def test_signin(self):
#正常登录
		client = Client()
		python_dict = {
				'username': 'walikrence',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)
#重复登录
		python_dict = {
				'username': 'ewwe123123ce',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 0)
#登陆后注册
		python_dict = {
				'username': 'dafasdrence',
				'password': '123456',
				'email' : '123456@qq.com'
			}
		response = client.post('/users/register/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 0)

	def test_signin_wrong_passwd(self):
#密码错误
		client = Client()
		python_dict = {
				'username': 'walikrence',
				'password': "123sfds56"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)
	def test_signin_wrong_username(self):
#用户不存在
		client = Client()
		python_dict = {
				'username': 'walikasdfasdrence',
				'password': "123sfds56"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)

	def test_register(self):
		client = Client()
#用户名已存在
		python_dict = {
				'username': 'walikrence',
				'password': '123456',
				'email' : '123456@qq.com'
			}
		response = client.post('/users/register/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)
#正常注册
		python_dict = {
				'username': 'dafasdrence',
				'password': '123456',
				'email' : '123456@qq.com'
			}
		response = client.post('/users/register/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)
#用户名已存在
		python_dict = {
				'username': 'dafasdrence',
				'password': '123456',
				'email' : '123456@qq.com'
			}
		response = client.post('/users/register/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)
#注册后登陆
		python_dict = {
				'username': 'dafasdrence',
				'password': '123456',
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)
	def test_signout(self):
		client = Client()
#登陆前使用退出登陆
		python_dict = {
					'username': 'walikrence'
				}
		response = client.post('/users/signout/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)
#正常登录

		python_dict = {
				'username': 'walikrence',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)
#正常退出
		python_dict = {
				'username': 'walikrence'
			}
		response = client.post('/users/signout/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)
















