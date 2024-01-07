from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# функции = обработчики запросов = контроллеры = вьюхи

def index(request) -> HttpResponse:
    context: dict ={
        'title': 'Home',
        'content': 'Hello World!'
    }
    return render(request, 'products/index.html', context)

def products(request):
    return HttpResponse('About page')