from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import transaction
from .models import Paper
from .models import Question_select
from .models import Option
from .models import Question_fill
from .models import Question_fill_answer
from .models import Option_vote

# Create your views here.

@csrf_exempt
@transaction.atomic
def query(request):
	if request.method == 'POST':
		message = '醒醒，你还没登陆呢'
		if not request.session.get('is_signin'):
			resp = {'message': message,'code' : 1}
			return HttpResponse(json.dumps(resp), content_type="application/json")
		else:
			message = '查询问卷成功'
			resp = {
			'message': message,
			'code' : 2
			}

			pl = list()

			paper = Paper.objects.all()[:10]
			paper_num = 0
			pl = list()
			for p in paper:
				paper_num = paper_num + 1

				pd = dict()
				p_id = p.id
				title = p.title
				select_question_num = p.select_question_num
				fill_question_num = p.fill_question_num
				creater = p.creater

				pd['id'] = p_id
				pd['title'] = title
				pd['select_question_num'] = select_question_num
				pd['fill_question_num'] = fill_question_num
				pd['creater'] = creater

				question = Question_select.objects.filter(paper=p)
				ql = list()

				for q in question:
					qd = dict()
					title = q.title
					option_num = q.option_num
					mytype = q.mytype
					qs_id = q.id

					qd['id'] = qs_id
					qd['title'] = title
					qd['option_num'] = option_num
					qd['mytype'] = mytype
					qd['option'] = list()

					option = Option.objects.filter(question=q)
					for o in option:
						od = dict()
						text = o.text
						vote_num = o.vote_num
						o_id = o.id

						od['text'] = text
						od['vote_num'] = vote_num
						od['id'] = o_id

						qd['option'].append(od)
					ql.append(qd)

				pd['Question_select'] = ql

				question_fill = Question_fill.objects.filter(paper=p)
				ql = list()
				for qf in question_fill:
					qd = dict()
					title = qf.title
					qf_id = qf.id
					qd['title'] = title
					qd['id'] = qf_id
					ql.append(qd)
				pd['Question_fill'] = ql

				pl.append(pd)
			resp['paper_num'] = paper_num
			resp['paper_list'] = pl


			
			return HttpResponse(json.dumps(resp), content_type="application/json")
	return HttpResponse("Hello, world. You're at the query paper.")

@csrf_exempt
@transaction.atomic
def create(request):
	if request.method == 'POST':
		message = '醒醒，你还没登陆呢'
		if not request.session.get('is_signin'):
			resp = {'message': message,'code' : 1}
			return HttpResponse(json.dumps(resp), content_type="application/json")
		else:
			try:
				received_json_data = json.loads(request.body)
				p_title = received_json_data.get('title')
				select_question_num = received_json_data.get('select_question_num')
				fill_question_num = received_json_data.get('fill_question_num')
				question_select = received_json_data.get('Question_select')
				question_fill = received_json_data.get('Question_fill')
				creater = request.session['user_name']

				p = Paper(title=p_title, select_question_num=select_question_num, fill_question_num=fill_question_num, creater=creater)
				p.save()
				#选择题
				if select_question_num > 0:
					for q in question_select:
						qs_title = q.get('title')
						option_num = q.get('option_num')
						mytype = q.get('mytype')
						option = q.get('option')
						q1 = Question_select(paper=p, title=qs_title, option_num=option_num, mytype=mytype)
						q1.save()
						if option_num >0:
							for o in option:
								text = o.get('text')
								o1 = Option(question=q1, text=text, vote_num=0)
								o1.save()
				#填空题
				if fill_question_num > 0:
					for q in question_fill:
						qf_title = q.get('title')
						q1 = Question_fill(paper=p, title=qf_title)
						q1.save()
			except :
				message = '格式不正确'
				resp = {'message': message,'code' : 2}
				return HttpResponse(json.dumps(resp), content_type="application/json")
			else:
				message = '创建成功'
				resp = {'message': message,'code' : 3,
				'title':p_title
				}
				return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		return HttpResponse("Hello, world. You're at the create paper.")

@csrf_exempt
@transaction.atomic
def delete(request):
	if request.method == 'POST':
		message = '醒醒，你还没登陆呢'
		if not request.session.get('is_signin'):
			resp = {'message': message,'code' : 1}
			return HttpResponse(json.dumps(resp), content_type="application/json")
		else:
			received_json_data = json.loads(request.body)
			title = received_json_data.get('title')
			p_id = received_json_data.get('id')
			user = request.session['user_name']
			try:
				p = Paper.objects.get(id=p_id)
			except :
				message = '没有这张问卷'
				resp = {'message': message,'code' : 2}
				return HttpResponse(json.dumps(resp), content_type="application/json")
			else:
				if p.creater == user:
					Paper.objects.get(id=p_id).delete()
					message = '删除成功'
					resp = {'message': message,'code' : 3}
					return HttpResponse(json.dumps(resp), content_type="application/json")
					#删除操作
				else:
					message = '您不是本问卷的创建者，无法删除'
					resp = {'message': message,'code' : 4}
					return HttpResponse(json.dumps(resp), content_type="application/json")

	return HttpResponse("Hello, world. You're at the delete paper.")

@csrf_exempt
@transaction.atomic
def fill(request):
	if request.method == 'POST':
		message = '醒醒，你还没登陆呢'
		if not request.session.get('is_signin'):
			resp = {'message': message,'code' : 1}
			return HttpResponse(json.dumps(resp), content_type="application/json")
		else:
			received_json_data = json.loads(request.body)
			p_id = received_json_data.get('id')
			question_select = received_json_data.get('Question_select')
			question_fill = received_json_data.get('Question_fill')

			i = len(question_select)
			while (i > 0):
				i = i - 1
				qs = question_select[i]
				qs_id = qs.get('id')
				mytype = qs.get('mytype')
				ol = qs.get('option')
				j = len(ol)
				while (j > 0):
					j = j - 1
					o = ol[j]
					o_id = o.get('id')
					is_select = o.get('is_select')
					if (is_select == 'yes'):

						try:
							option = Option.objects.get(id = o_id)
							voter = request.session['user_name'] 
						except :
							message = '格式不正确'
							resp = {'message': message,'code' : 2}
							return HttpResponse(json.dumps(resp), content_type="application/json")
						else:
							option.vote_num = option.vote_num + 1
							# print(option.id)
							# print(option.vote_num)
							option.save()
							o_v = Option_vote(option=option, voter=voter)
							o_v.save()


			i = len(question_fill)
			while (i > 0):
				i = i -1
				qf = question_fill[i]
				qf_id = qf.get('id')
				answer = qf.get('answer')
				author = request.session['user_name'] 
				try:
					question = Question_fill.objects.get(id = qf_id)
				except:
					message = '格式不正确'
					resp = {'message': message,'code' : 2}
					return HttpResponse(json.dumps(resp), content_type="application/json")
				else:
					question_fill_answer = Question_fill_answer(question = question, answer=answer, author=author )
					question_fill_answer.save()

			message = '提交成功'
			resp = {'message': message,'code' : 3}
			return HttpResponse(json.dumps(resp), content_type="application/json")

	return HttpResponse("Hello, world. You're at the delete paper.")
















