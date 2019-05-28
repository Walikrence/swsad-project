from django.test import TestCase
from .models import User
from django.test import Client
from django.test.utils import setup_test_environment
import json


class mytes(TestCase):


	def test_mytes(self):
		u = User(username="walikrence", password="123456")
		u.save()
		client = Client()
		python_dict = {
				"account": "walikrence",
				"password": "123456"
			}
		response = client.post('/users/signin',json.dumps(python_dict),content_type="application/json")
		send_json_data = json.loads(response.content)
		self.assertEqual(send_json_data.get("status"), 'success')



# def test_your_test(self):
#     python_dict = {
#         "1": {
#             "guid": "8a40135230f21bdb0130f21c255c0007",
#             "portalId": 999,
#             "email": "fake@email"
#         }
#     }
#     response = self.client.post('/pipeline-endpoint/',
#                                 json.dumps(python_dict),
#                                 content_type="application/json")

# class QuestionModelTests(TestCase):

#     def test_was_published_recently_with_future_question(self):
#         """
#         was_published_recently() returns False for questions whose pub_date
#         is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)