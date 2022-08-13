from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def say_hello(request):
    return render(request, 'hello.html', {'name': 'DaGreat!'})