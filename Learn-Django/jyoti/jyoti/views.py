from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    
    return render(request,'intex.html')
 #HttpResponse("HELLO , WORLD. you are at shop home cycle")

def about(request):
    return HttpResponse("HELLO , WORLD. you are at shop cycle")

def contact(request):
     return HttpResponse("HELLO , WORLD. you are at shop about cycle")




