from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def russell(request):
    return HttpResponse('<h1>welcome russell</>')
