
from django.urls import path
from . import views

# localhost 8000/giri
urlpatterns = [
    path('',views.all_giri,),
    path('all_giri/', views.all_giri,),
]