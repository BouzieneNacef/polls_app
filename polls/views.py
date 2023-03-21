from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello this the first views")

# Create your views here.
