from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.profiles_form,name='add_profile'),
    
]