from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World. You are viewing polls index page')
