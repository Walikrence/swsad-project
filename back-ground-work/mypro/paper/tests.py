from django.test import TestCase
from users.models import User
from django.test import Client
from django.test.utils import setup_test_environment
import json
from .models import Paper
from .models import Question_select
from .models import Option
from .models import Question_fill
from .models import Question_fill_answer
from .models import Option_vote


# Create your tests here.
class TEST_PAPER(TestCase):
	def setUp(self):
		u = User(name='walikrence', password="123456")
		u.save()
		u = User(name='lyre', password="123456")
		u.save()
		p = Paper(title = '问卷一', select_question_num=2, fill_question_num=1, creater='walikrence')
		p.save()
		qs1 = Question_select(paper=p, title='多选题', option_num=3, mytype='单选')
		qs1.save()
		qs2 =Question_select(paper=p, title='单选题', option_num=3, mytype='多选')
		qs2.save()
		qs1_op1 = Option(question=qs1,text='多选题-选项1',vote_num=0)
		qs1_op1.save()
		qs1_op2 = Option(question=qs1,text='多选题-选项2',vote_num=0)
		qs1_op2.save()
		qs1_op3 = Option(question=qs1,text='多选题-选项3',vote_num=0)
		qs1_op3.save()
		qs2_op1 = Option(question=qs2,text='单选题-选项1',vote_num=0)
		qs2_op1.save()
		qs2_op2 = Option(question=qs2,text='单选题-选项2',vote_num=0)
		qs2_op2.save()
		qs2_op3 = Option(question=qs2,text='单选题-选项3',vote_num=0)
		qs2_op3.save()
		qf = Question_fill(paper=p, title='填空题',)
		qf.save()

	def test_query(self):
#正常登录
		client = Client()
		python_dict = {
				'username': 'walikrence',
				'password': "123456"
			}
		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)

		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)
		# print(send_json_data)

	def test_create_paper(self):
		client = Client()
		python_dict = {
				'username': 'walikrence',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		python_dict = {
		    "title": "问卷二", 
		    "select_question_num": 2, 
		    "fill_question_num": 1, 
		    "Question_select": [
		        {
		            "title": "新多选题", 
		            "option_num": 3, 
		            "mytype": "单选", 
		            "option": [
		                {
		                    "text": "新多选题-选项1", 
		                }, 
		                {
		                    "text": "新多选题-选项2", 
		                }, 
		                {
		                    "text": "新多选题-选项3", 
		                }
		            ]
		        }, 
		        {
		            "title": "新单选题", 
		            "option_num": 3, 
		            "mytype": "多选", 
		            "option": [
		                {
		                    "text": "新单选题-选项1", 
		                }, 
		                {
		                    "text": "新单选题-选项2", 
		                }, 
		                {
		                    "text": "新单选题-选项3", 
		                }
		            ]
		        }
		    ], 
		    "Question_fill": [
		        {
		            "title": "新填空题"
		        }
		    ]
		}
		response = client.post('/paper/create/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)

		response = client.post('/paper/create/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)
		# print(send_json_data)

		python_dict = {
				'username': 'walikrence'
			}
		response = client.post('/users/signout/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

	def test_create_paper_not_signin(self):
		client = Client()
		python_dict = {
		    "title": "问卷二", 
		    "select_question_num": 2, 
		    "fill_question_num": 1, 
		    "Question_select": [
		        {
		            "title": "新多选题", 
		            "option_num": 3, 
		            "mytype": "单选", 
		            "option": [
		                {
		                    "text": "新多选题-选项1", 
		                }, 
		                {
		                    "text": "新多选题-选项2", 
		                }, 
		                {
		                    "text": "新多选题-选项3", 
		                }
		            ]
		        }, 
		        {
		            "title": "新单选题", 
		            "option_num": 3, 
		            "mytype": "多选", 
		            "option": [
		                {
		                    "text": "新单选题-选项1", 
		                }, 
		                {
		                    "text": "新单选题-选项2", 
		                }, 
		                {
		                    "text": "新单选题-选项3", 
		                }
		            ]
		        }
		    ], 
		    "Question_fill": [
		        {
		            "title": "新填空题"
		        }
		    ]
		}
		response = client.post('/paper/create/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)

	def test_create_paper_no_fill_question(self):
		client = Client()
		python_dict = {
				'username': 'walikrence',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		python_dict = {
		    "title": "问卷二", 
		    "select_question_num": 2, 
		    "fill_question_num": 0, 
		    "Question_select": [
		        {
		            "title": "新多选题", 
		            "option_num": 3, 
		            "mytype": "单选", 
		            "option": [
		                {
		                    "text": "新多选题-选项1", 
		                }, 
		                {
		                    "text": "新多选题-选项2", 
		                }, 
		                {
		                    "text": "新多选题-选项3", 
		                }
		            ]
		        }, 
		        {
		            "title": "新单选题", 
		            "option_num": 3, 
		            "mytype": "多选", 
		            "option": [
		                {
		                    "text": "新单选题-选项1", 
		                }, 
		                {
		                    "text": "新单选题-选项2", 
		                }, 
		                {
		                    "text": "新单选题-选项3", 
		                }
		            ]
		        }
		    ]
		}
		response = client.post('/paper/create/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)

	def test_delete(self):
		client = Client()
		python_dict = {
				'username': 'walikrence',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		title = paper.get('title')
		id = paper.get('id')

		python_dict = {
				'title': title,
				'id': id
			}
		response = client.post('/paper/delete/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)

		python_dict = {
				'title': title,
				'id': id
			}
		response = client.post('/paper/delete/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		python_dict = {
		    "title": "问卷二", 
		    "select_question_num": 2, 
		    "fill_question_num": 1, 
		    "Question_select": [
		        {
		            "title": "新多选题", 
		            "option_num": 3, 
		            "mytype": "单选", 
		            "option": [
		                {
		                    "text": "新多选题-选项1", 
		                }, 
		                {
		                    "text": "新多选题-选项2", 
		                }, 
		                {
		                    "text": "新多选题-选项3", 
		                }
		            ]
		        }, 
		        {
		            "title": "新单选题", 
		            "option_num": 3, 
		            "mytype": "多选", 
		            "option": [
		                {
		                    "text": "新单选题-选项1", 
		                }, 
		                {
		                    "text": "新单选题-选项2", 
		                }, 
		                {
		                    "text": "新单选题-选项3", 
		                }
		            ]
		        }
		    ], 
		    "Question_fill": [
		        {
		            "title": "新填空题"
		        }
		    ]
		}
		response = client.post('/paper/create/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		title = paper.get('title')
		id = paper.get('id')

		python_dict = {
				'title': title,
				'id': id
			}
		response = client.post('/paper/delete/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)


	def test_delete_not_signin(self):
		client = Client()
		python_dict = {
				'username': 'walikrence',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		title = paper.get('title')
		id = paper.get('id')

		python_dict = {
				'username': 'walikrence'
			}
		response = client.post('/users/signout/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		python_dict = {
				'title': title,
				'id': id
			}
		response = client.post('/paper/delete/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)

	def test_delete_not_creater(self):
		client = Client()
		python_dict = {
				'username': 'lyre',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		title = paper.get('title')
		id = paper.get('id')
		python_dict = {
				'title': title,
				'id': id
			}
		response = client.post('/paper/delete/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 4)

	def test_fill(self):
		client = Client()
		python_dict = {
				'username': 'lyre',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		p_id = paper.get('id')
		self.assertEqual(p_id, 1)

		p_id = paper.get('id')
		qs1 = paper.get('Question_select')[0]
		qs1_id = qs1.get('id')
		ol = qs1.get('option')
		o1_id = ol[0].get('id')
		o2_id = ol[1].get('id')
		o3_id = ol[2].get('id')
		o1_vote_num = ol[0].get('vote_num')
		o2_vote_num = ol[1].get('vote_num')
		o3_vote_num = ol[2].get('vote_num')
		qs2 = paper.get('Question_select')[1]
		qs2_id = qs2.get('id')
		ol = qs2.get('option')
		o4_id = ol[0].get('id')
		o5_id = ol[1].get('id')
		o6_id = ol[2].get('id')
		o4_vote_num = ol[0].get('vote_num')
		o5_vote_num = ol[1].get('vote_num')
		o6_vote_num = ol[2].get('vote_num')
		qf = paper.get('Question_fill')[0]
		qf_id = qf.get('id')
		answer = '这是我提交的答案'
		self.assertEqual(p_id, 1)
		self.assertEqual(qs1_id, 1)
		self.assertEqual(o1_id, 1)
		self.assertEqual(o2_id, 2)
		self.assertEqual(o3_id, 3)
		self.assertEqual(qs2_id, 2)
		self.assertEqual(o4_id, 4)
		self.assertEqual(o5_id, 5)
		self.assertEqual(o6_id, 6)
		self.assertEqual(qf_id, 1)

		self.assertEqual(o1_vote_num, 0)
		self.assertEqual(o2_vote_num, 0)
		self.assertEqual(o3_vote_num, 0)
		self.assertEqual(o4_vote_num, 0)
		self.assertEqual(o5_vote_num, 0)
		self.assertEqual(o6_vote_num, 0)

		python_dict = {
		    'id': p_id,
		    "Question_select": [
		        {
		        	'id': qs1_id,
		            "option": [
		                {
		                    'id': o1_id,
		                    'is_select':'no' 
		                }, 
		                {
		                    'id': o2_id,
		                    'is_select':'yes' 
		                }, 
		                {
		                    'id': o3_id,
		                    'is_select':'no' 
		                }
		            ]
		        }, 
		        {
		        	'id':qs2_id,
		            "option": [
		                {
		                    'id': o4_id,
		                    'is_select':'no'  
		                }, 
		                {
		                    'id': o5_id,
		                    'is_select':'yes' 
		                }, 
		                {
		                    'id': o6_id,
		                    'is_select':'yes'  
		                }
		            ]
		        }
		    ], 
		    "Question_fill": [
		        {
		            'id': qf_id,
		            'answer': answer
		        }
		    ]
		}

		response = client.post('/paper/fill/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 3)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		p_id = paper.get('id')
		self.assertEqual(p_id, 1)

		qs1 = paper.get('Question_select')[0]
		ol = qs1.get('option')
		o1_vote_num = ol[0].get('vote_num')
		o2_vote_num = ol[1].get('vote_num')
		o3_vote_num = ol[2].get('vote_num')
		qs2 = paper.get('Question_select')[1]
		ol = qs2.get('option')
		o4_vote_num = ol[0].get('vote_num')
		o5_vote_num = ol[1].get('vote_num')
		o6_vote_num = ol[2].get('vote_num')

		self.assertEqual(o1_vote_num, 0)
		self.assertEqual(o2_vote_num, 1)
		self.assertEqual(o3_vote_num, 0)
		self.assertEqual(o4_vote_num, 0)
		self.assertEqual(o5_vote_num, 1)
		self.assertEqual(o6_vote_num, 1)

	def test_fill_wrong_format(self):
		client = Client()
		python_dict = {
				'username': 'lyre',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		p_id = paper.get('id')
		self.assertEqual(p_id, 1)

		p_id = paper.get('id')
		qs1 = paper.get('Question_select')[0]
		qs1_id = qs1.get('id')
		ol = qs1.get('option')
		o1_id = ol[0].get('id')
		o2_id = ol[1].get('id')
		o3_id = ol[2].get('id')
		o1_vote_num = ol[0].get('vote_num')
		o2_vote_num = ol[1].get('vote_num')
		o3_vote_num = ol[2].get('vote_num')
		qs2 = paper.get('Question_select')[1]
		qs2_id = qs2.get('id')
		ol = qs2.get('option')
		o4_id = ol[0].get('id')
		o5_id = ol[1].get('id')
		o6_id = ol[2].get('id')
		o4_vote_num = ol[0].get('vote_num')
		o5_vote_num = ol[1].get('vote_num')
		o6_vote_num = ol[2].get('vote_num')
		qf = paper.get('Question_fill')[0]
		qf_id = qf.get('id')
		answer = '这是我提交的答案'
		self.assertEqual(p_id, 1)
		self.assertEqual(qs1_id, 1)
		self.assertEqual(o1_id, 1)
		self.assertEqual(o2_id, 2)
		self.assertEqual(o3_id, 3)
		self.assertEqual(qs2_id, 2)
		self.assertEqual(o4_id, 4)
		self.assertEqual(o5_id, 5)
		self.assertEqual(o6_id, 6)
		self.assertEqual(qf_id, 1)

		self.assertEqual(o1_vote_num, 0)
		self.assertEqual(o2_vote_num, 0)
		self.assertEqual(o3_vote_num, 0)
		self.assertEqual(o4_vote_num, 0)
		self.assertEqual(o5_vote_num, 0)
		self.assertEqual(o6_vote_num, 0)

		python_dict = {
		    'id': p_id,
		    "Question_select": [
		        {
		        	'id': qs1_id,
		            "option": [
		                {
		                    'id': o1_id,
		                    'is_select':'no' 
		                }, 
		                {
		                    'id': o2_id,
		                    'is_select':'yes' 
		                }, 
		                {
		                    'id': o3_id,
		                    'is_select':'no' 
		                }
		            ]
		        }, 
		        {
		        	'id':qs2_id,
		            "option": [
		                {
		                    'id': o4_id,
		                    'is_select':'no'  
		                }, 
		                {
		                    'id': o5_id,
		                    'is_select':'yes' 
		                }, 
		                {
		                    'id': 100,
		                    'is_select':'yes'  
		                }
		            ]
		        }
		    ], 
		    "Question_fill": [
		        {
		            'id': qf_id,
		            'answer': answer
		        }
		    ]
		}

		response = client.post('/paper/fill/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		p_id = paper.get('id')
		self.assertEqual(p_id, 1)

		qs1 = paper.get('Question_select')[0]
		ol = qs1.get('option')
		o1_vote_num = ol[0].get('vote_num')
		o2_vote_num = ol[1].get('vote_num')
		o3_vote_num = ol[2].get('vote_num')
		qs2 = paper.get('Question_select')[1]
		ol = qs2.get('option')
		o4_vote_num = ol[0].get('vote_num')
		o5_vote_num = ol[1].get('vote_num')
		o6_vote_num = ol[2].get('vote_num')

		self.assertEqual(o1_vote_num, 0)
		self.assertEqual(o2_vote_num, 0)
		self.assertEqual(o3_vote_num, 0)
		self.assertEqual(o4_vote_num, 0)
		self.assertEqual(o5_vote_num, 0)
		self.assertEqual(o6_vote_num, 0)
	def test_fill_not_signin(self):
		client = Client()
		python_dict = {
				'username': 'lyre',
				'password': "123456"
			}
		response = client.post('/users/signin/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		p_id = paper.get('id')
		self.assertEqual(p_id, 1)

		p_id = paper.get('id')
		qs1 = paper.get('Question_select')[0]
		qs1_id = qs1.get('id')
		ol = qs1.get('option')
		o1_id = ol[0].get('id')
		o2_id = ol[1].get('id')
		o3_id = ol[2].get('id')
		o1_vote_num = ol[0].get('vote_num')
		o2_vote_num = ol[1].get('vote_num')
		o3_vote_num = ol[2].get('vote_num')
		qs2 = paper.get('Question_select')[1]
		qs2_id = qs2.get('id')
		ol = qs2.get('option')
		o4_id = ol[0].get('id')
		o5_id = ol[1].get('id')
		o6_id = ol[2].get('id')
		o4_vote_num = ol[0].get('vote_num')
		o5_vote_num = ol[1].get('vote_num')
		o6_vote_num = ol[2].get('vote_num')
		qf = paper.get('Question_fill')[0]
		qf_id = qf.get('id')
		answer = '这是我提交的答案'
		self.assertEqual(p_id, 1)
		self.assertEqual(qs1_id, 1)
		self.assertEqual(o1_id, 1)
		self.assertEqual(o2_id, 2)
		self.assertEqual(o3_id, 3)
		self.assertEqual(qs2_id, 2)
		self.assertEqual(o4_id, 4)
		self.assertEqual(o5_id, 5)
		self.assertEqual(o6_id, 6)
		self.assertEqual(qf_id, 1)

		self.assertEqual(o1_vote_num, 0)
		self.assertEqual(o2_vote_num, 0)
		self.assertEqual(o3_vote_num, 0)
		self.assertEqual(o4_vote_num, 0)
		self.assertEqual(o5_vote_num, 0)
		self.assertEqual(o6_vote_num, 0)

		python_dict = {
		    'id': p_id,
		    "Question_select": [
		        {
		        	'id': qs1_id,
		            "option": [
		                {
		                    'id': o1_id,
		                    'is_select':'no' 
		                }, 
		                {
		                    'id': o2_id,
		                    'is_select':'yes' 
		                }, 
		                {
		                    'id': o3_id,
		                    'is_select':'no' 
		                }
		            ]
		        }, 
		        {
		        	'id':qs2_id,
		            "option": [
		                {
		                    'id': o4_id,
		                    'is_select':'no'  
		                }, 
		                {
		                    'id': o5_id,
		                    'is_select':'yes' 
		                }, 
		                {
		                    'id': 100,
		                    'is_select':'yes'  
		                }
		            ]
		        }
		    ], 
		    "Question_fill": [
		        {
		            'id': qf_id,
		            'answer': answer
		        }
		    ]
		}

		response = client.post('/paper/fill/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/query/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		paper= send_json_data.get('paper_list')[0]
		p_id = paper.get('id')
		self.assertEqual(p_id, 1)

		qs1 = paper.get('Question_select')[0]
		ol = qs1.get('option')
		o1_vote_num = ol[0].get('vote_num')
		o2_vote_num = ol[1].get('vote_num')
		o3_vote_num = ol[2].get('vote_num')
		qs2 = paper.get('Question_select')[1]
		ol = qs2.get('option')
		o4_vote_num = ol[0].get('vote_num')
		o5_vote_num = ol[1].get('vote_num')
		o6_vote_num = ol[2].get('vote_num')

		self.assertEqual(o1_vote_num, 0)
		self.assertEqual(o2_vote_num, 0)
		self.assertEqual(o3_vote_num, 0)
		self.assertEqual(o4_vote_num, 0)
		self.assertEqual(o5_vote_num, 0)
		self.assertEqual(o6_vote_num, 0)

		python_dict2 = {
				'username': 'walikrence'
			}
		response = client.post('/users/signout/',json.dumps(python_dict2),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 2)

		response = client.post('/paper/fill/',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get('code'), 1)






	# def test_database(self):
	# 	paper = Paper.objects.all()[:10]
	# 	for p in paper:
	# 		question = Question_select.objects.filter(paper=p)
	# 		for q in question:
	# 			title = q.title
	# 			option_num = q.option_num
	# 			mytype = q.mytype
	# 			print(title)
	# 			print(option_num)
	# 			print(mytype)
	# 			option = Option.objects.filter(question=q)
	# 			for o in option:
	# 				text = o.text
	# 				vote_num = o.vote_num
	# 				print(text)
	# 				print(vote_num)
	# 		question_fill = Question_fill.objects.filter(paper=p)
	# 		for qf in question_fill:
	# 			title = qf.title
	# 			print(title)





























