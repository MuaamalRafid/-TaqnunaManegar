from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('input',views.empoinput,name="input"),
    path('inputeams',views.teams,name="teams"),
]