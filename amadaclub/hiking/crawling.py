import requests
import xmltodict
from amadaclub.settings import *
import time
import datetime
import json


def mountain_weather():
    keyValue = env('MOUTAIN_API_KEY')
    now = time.strftime('%Y%m%d%H')
    if datetime.datetime.now().second > 40:
        now += '30'
    # now_time = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+str(now.tm_hour)+str(now.tm_min)+str(now.tm_sec)
    url = "http://know.nifos.go.kr/openapi/mtweather/mountListSearch.do?keyValue="+keyValue+"&version=1.0&localArea=&obsid=ALL&tm="+now
    req = requests.get(url).content
    xmlObject = xmltodict.parse(req) #XML형태
    xmlObject_json = json.dumps(xmlObject) #json 형태
    allData = json.loads(xmlObject_json) #dict 형태
    return allData['metadata']['outputData']['items']

def address():
    with open('static/json/mountain.json', encoding='utf-8') as json_file:
        addresses = json.load(json_file)
    addressDict = []
    for address in addresses:
        if address.get('location'):
            content = {
                'mountain':address['mountain'],
                'mapx':str(address['mapx']),
                'mapy':str(address['mapy'])
            }
            addressDict.append(content)

    addressJson = json.dumps(addressDict, ensure_ascii=False)
    return addressJson

# 지역
#     공백 : 전체
# 01 : 서울특별시
# 02 : 세종특별자치시
# 03 : 부산광역시
# 04 : 대구광역시
# 05 : 광주광역시
# 06 : 인천광역시
# 07 : 대전광역시
# 08 : 울산광역시
# 09 : 경기도
# 10 : 강원도
# 11 : 충청남도
# 12 : 충청북도
# 13 : 전라남도
# 14 : 전라북도
# 15 : 경상남도
# 16 : 경상북도
# 17 : 제주도