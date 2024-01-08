from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# функции = обработчики запросов = контроллеры = вьюхи

def index(request) -> HttpResponse:
    context: dict ={
        'title': 'Home - first page',
        'content': 'Hello World!',
        'product': 'Social Media',
        'white': 'White people - is a great person'
    }

    return render(request, 'products/index.html', context)

def products(request):
    return render(request, 'products/products.html')