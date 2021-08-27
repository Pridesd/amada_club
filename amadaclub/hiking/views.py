from django.shortcuts import render
from django.http import request

def hiking(request):
    return render(request, 'hiking.html')

# Create your views here.
