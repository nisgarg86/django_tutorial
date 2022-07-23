from django.http import HttpResponse
from django.template import loader

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context_dict = {'latest_question_list': latest_question_list}
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context_dict, request))


def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are looking at results of question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting for question {question_id}')
