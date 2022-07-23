from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context_dict = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context_dict)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse(f'You are looking at results of question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting for question {question_id}')
