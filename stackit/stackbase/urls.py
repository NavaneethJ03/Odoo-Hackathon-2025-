from django.urls import path , include 
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.home, name='home'),
]
