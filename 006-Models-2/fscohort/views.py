from django.shortcuts import render


from django.http import HttpResponse
def home(request):
    return HttpResponse('Hello. Welcome.')

def fscohort(request):
    return HttpResponse('Now, you are in fscohort.')

def subfolder(request):
    return HttpResponse('Now, you are in subfolder.')