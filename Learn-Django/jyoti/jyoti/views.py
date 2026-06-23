from django.http import HttpResponse


def home(request):
    return HttpResponse("HELLO , WORLD. you are at shop home cycle")

def about(request):
    return HttpResponse("HELLO , WORLD. you are at shop cycle")

def contact(request):
     return HttpResponse("HELLO , WORLD. you are at shop about cycle")




