from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.


def index(request):
    return HttpResponse("Thiss is my homepage")

def home(request):
    return HttpResponse ("Thiss is my homepage")
