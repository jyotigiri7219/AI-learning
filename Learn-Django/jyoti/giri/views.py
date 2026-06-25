from django.shortcuts import render

# Create your views here.
def all_giri(request):
    return render(request, 'giri/all_Giri.html')
