from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name = "home"),
    path('about_us/', about_us, name="about_us")
]