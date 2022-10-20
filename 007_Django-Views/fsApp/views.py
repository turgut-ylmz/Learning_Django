from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def home(request):
#     print(request)
#     print(request.method)
#     print(request.COOKIES)
#     print(request.path)
#     print(request.user)
#     print(request.META)
  
#     html="<html><body>hello FS</body></html>"
#     return HttpResponse(html)

def home(request):
    context = {
        'caption': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request,'fsApp/index.html',context)