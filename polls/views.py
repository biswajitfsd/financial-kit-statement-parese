from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello World! I am here to learn Python")