from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def home(request):
#     print(request)
#     print(request.method)
#     print(request.COOKIES)
    
    
    
#     html="<html><body> Hallo Leute!</body></html>"
#     return HttpResponse(html)

def home(request):
    return render(request, 'dsApp/index.html')