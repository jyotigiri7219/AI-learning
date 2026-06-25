
from django.urls import path
from . import views

# localhost 8000/giri
urlpatterns = [
    path('',views.home),
]