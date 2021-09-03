from django.shortcuts import render
from django.http import request
from .crawling import *

def hiking(request):
    weather = mountain_weather(1)
    temp = {}
    wind = {}
    humanity = {}
    rain = {}
    for number in range(len(weather)):
        temp[weather[number]["obsname"]] = weather[number]['tm2m'] #기온
        humanity[weather[number]["obsname"]] = weather[number]['hm2m'] #습도
        wind[weather[number]["obsname"]] = weather[number]['ws2m'] #풍속
        rain[weather[number]["obsname"]] = weather[number]['rn'] #강수량
    weather_result = {'temp':temp, 'wind':wind, 'humanity':humanity, 'rain':rain}
    return render(request, 'hiking.html', weather_result)

# Create your views here.
