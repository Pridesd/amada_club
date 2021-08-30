from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', community, name="community"),
    path('detail/<str:id>', co_detail, name = "co_detail"),
    path('new/', co_new, name = "co_new"),
    path('create/', co_create, name="co_create"),
    path('edit/<str:id>', co_edit, name="co_edit"),
    path('update/<str:id>', co_update, name = "co_update"),
    path('delete/<str:id>', co_delete, name = "co_delete"),
    path('ask/<str:id>', co_ask, name="co_ask"),
]