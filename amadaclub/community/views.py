from django.shortcuts import render
from django.http import request

def community(request):
    return render(request, 'community.html')

# Create your views here.
