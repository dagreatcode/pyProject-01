from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def say_hello(request):
    return render(request, 'hello.html', {'name': 'DaGreat!'})

def test(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')