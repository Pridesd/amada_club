from django.shortcuts import render
from django.http import request
from .crawling import *

def hiking(request):
    weather = mountain_weather()
    weatherDict = []
    for number in range(len(weather)):
        content = {
        'mountain': weather[number]["obsname"],
        'temp':weather[number]['tm2m'],
        'humanity':weather[number]['hm2m'],
        'wind': weather[number]['ws2m'],
        'rain':weather[number]['rn']
        }
        weatherDict.append(content)
    weatherJson = json.dumps(weatherDict, ensure_ascii=False)
    weather_result = {'weather':weatherJson, 'location':address()}
    return render(request, 'hiking.html', weather_result)

# Create your views here.
#weather[number]["obsname"]