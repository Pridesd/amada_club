import requests
import xmltodict
from amadaclub.settings import *
import time
import datetime
import json


def mountain_weather(location):
    keyValue = env('MOUTAIN_API_KEY')
    loca = str(location)
    now = time.strftime('%Y%m%d%H')
    if datetime.datetime.now().second > 40:
        now += '30'
    # now_time = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+str(now.tm_hour)+str(now.tm_min)+str(now.tm_sec)
    url = "http://know.nifos.go.kr/openapi/mtweather/mountListSearch.do?keyValue="+keyValue+"&version=1.0&localArea=01&tm="+now
    req = requests.get(url).content
    xmlObject = xmltodict.parse(req) #XML형태
    xmlObject_json = json.dumps(xmlObject) #json 형태
    allData = json.loads(xmlObject_json) #dict 형태
    return allData['metadata']['outputData']['items']

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

#지점번호
# 전체	공백

# 서울특별시	홍릉수목원임외	1910
# 서울특별시	홍릉수목원임내	1911
# 서울특별시	서울 천장산	1912
# 서울특별시	서울 용마산	1913
# 서울특별시	서울 봉산	1914
# 서울특별시	서울 개화산	1915
# 서울특별시	서울 구룡산	1916
# 서울특별시	서울 관악산	1917
# 서울특별시	서울 수락산	1918



# 세종특별자치시	세종 관불산	4910
# 세종특별자치시	세종 칠불산	4911



# 부산광역시	부산 양달산	8914
# 부산광역시	부산 백양산	8915



# 대전광역시	대전 계족산	4912
# 대전광역시	대전 보문산	4913



# 울산광역시	울산 능동산	8900
# 울산광역시	울주 백운산	8912



# 경기도	파주 팔일봉	1890
# 경기도	양평 금왕산	1891
# 경기도	양평 어비산	1892
# 경기도	양평 삼각산	1893
# 경기도	포천 한나무봉	1894
# 경기도	가평 서리산	1895
# 경기도	가평 청우산	1896
# 경기도	연천 밥재	1897
# 경기도	연천 고랑포	1898
# 경기도	파주 백학산	1899
# 경기도	연천 천덕산	1900
# 경기도	연천 밤고개	1901
# 경기도	용인 응봉	1902
# 경기도	남양주 용암산	1903
# 경기도	파주 비학산	1905
# 경기도	양평 소리산	1906
# 경기도	김포 문수산	1908
# 경기도	파주 월롱산	1909
# 경기도	여주 황학산	1919
# 경기도	화성 칠보산	1946
# 경기도	포천 운악산	1947
# 경기도	용인 바래기산	1948
# 경기도	여주 마감산	1949
# 경기도	가평 봉미산	2047



# 강원도	화천 성불령 용화산	2000
# 강원도	춘천 연엽산	2001
# 강원도	철원 흑운토령	2002
# 강원도	철원 곰배산	2003
# 강원도	고성 고황봉	2004
# 강원도	고성 까치봉	2005
# 강원도	고성 건봉산	2006
# 강원도	고성 죽변봉	2007
# 강원도	고성 성인대	2008
# 강원도	양구 봉화산	2009
# 강원도	양구 백석산	2010
# 강원도	영월 두위봉	2011
# 강원도	인제 가칠봉	2012
# 강원도	인제 대암산	2013
# 강원도	인제 원대봉	2014
# 강원도	정선 백석봉	2015
# 강원도	철원 은하봉	2016
# 강원도	철원 두목봉	2017
# 강원도	철원 흰바우산	2018
# 강원도	평창 백석산	2019
# 강원도	평창 중왕산	2020
# 강원도	화천 두류산	2021
# 강원도	화천 수리봉	2022
# 강원도	영월 망경대산	2023
# 강원도	영월 곰봉	2024
# 강원도	삼척 육백산	2025
# 강원도	강릉 피래산	2026
# 강원도	정선 중봉산	2027
# 강원도	강릉 화란봉	2028
# 강원도	정선 하봉	2029
# 강원도	정선 늑평산	2030
# 강원도	평창 매봉	2031
# 강원도	평창 청태산	2032
# 강원도	횡성 매봉산	2033
# 강원도	횡성 태기산	2034
# 강원도	춘천 느랏재	2035
# 강원도	춘천 사오랑골	2036
# 강원도	횡성 마당재골	2037
# 강원도	홍천 매화산	2038
# 강원도	홍천 까끈봉	2039
# 강원도	홍천 오음산	2040
# 강원도	홍천 응봉산	2041
# 강원도	춘천 금병산	2042
# 강원도	춘천 죽엽산	2043
# 강원도	춘천 토보산	2044
# 강원도	춘천 석파령	2045
# 강원도	춘천 뒷재봉	2046
# 강원도	화천 일산	2048
# 강원도	화천 오봉산	2049
# 강원도	철원 용봉산	2050
# 강원도	횡성 어답산	2051
# 강원도	강릉 고루포기산	2052
# 강원도	강릉 대궁산	2053
# 강원도	양양 시루봉	2054
# 강원도	평창 구양사골	2055
# 강원도	평창 능경봉	2056
# 강원도	평창 황병산	2057
# 강원도	정선 동강자연휴양림	2058
# 강원도	정선 꽃밭덩이산	2059
# 강원도	삼척 뇌암산	2060
# 강원도	삼척 깃대봉	2061
# 강원도	삼척 한오봉	2063
# 강원도	인제 아미산	2064
# 강원도	인제 명당산	2065
# 강원도	인제 응봉산	2066
# 강원도	인제 서리골	2067
# 강원도	양구 기룡산	2068
# 강원도	양구 사명산	2069
# 강원도	양구 천미골	2070
# 강원도	양구 검무정골	2071
# 강원도	양구 대우산	2072
# 강원도	양구 도솔산	2073
# 강원도	강릉 매봉산	2074
# 강원도	강릉 사달산	2075
# 강원도	평창 두타산	2076
# 강원도	평창 술이봉	2077
# 강원도	영월 도마니골	2078
# 강원도	정선 화절령	2079
# 강원도	정선 기추목이	2080
# 강원도	동해 앞재넘어골	2081
# 강원도	삼척 멍에산	2082
# 강원도	태백 풀장골	2083
# 강원도	강릉 곤신봉	2890
# 강원도	인제 한석산	2891
# 강원도	인제 가득봉	2892
# 강원도	홍천 불발령	2893
# 강원도	양양 감투봉	2894
# 강원도	강릉 전후재	2895
# 강원도	강릉 사기막	2896
# 강원도	강릉 제왕산	2897
# 강원도	강릉 만덕봉	2898
# 강원도	평창 선자령	2899
# 강원도	정선 가리왕산	2900
# 강원도	정선 봉화치	2901
# 강원도	정선 갈고개	2902
# 강원도	삼척 덕항산	2903
# 강원도	태백 함백산	2904
# 강원도	삼척 사금산	2905
# 강원도	영월 배향산	2906
# 강원도	횡성 사자산	2907
# 강원도	평창 남병산	2908
# 강원도	홍천 대학산	2909
# 강원도	춘천 가리산	2911
# 강원도	춘천 계관산	2912
# 강원도	삼척 상서기	2913
# 강원도	삼척 소공령	2914
# 강원도	삼척 헬기장	2915
# 강원도	삼척 검봉산	2916
# 강원도	삼척 중봉산	2917



# 충청남도	금산 성주산	4890
# 충청남도	부여 축융봉	4891
# 충청남도	공주 무성산	4892
# 충청남도	공주 국사봉	4893
# 충청남도	아산 광덕산	4894
# 충청남도	보령 오서산	4895
# 충청남도	청양비봉산	4896
# 충청남도	공주 장군산	4897
# 충청남도	천안 국사봉	4898
# 충청남도	논산 묘련봉	4899
# 충청남도	금산 성치산	4900
# 충청남도	금산 백암산	4901
# 충청남도	청양 대덕봉	4902
# 충청남도	아산 만경산	4903
# 충청남도	금산 운하산	4904
# 충청남도	청양 오봉산	4905
# 충청남도	천안 개죽산	4906
# 충청남도	천안 몽각산	4907
# 충청남도	공주 천태산	4908



# 충청북도	괴산 구석산	3022
# 충청북도	음성 개미산	3023
# 충청북도	충주 장병산	3024
# 충청북도	충주 오청산	3025
# 충청북도	충주 마미산	3026
# 충청북도	제천 갱승갱이재	3027
# 충청북도	단양 겸암산	3028
# 충청북도	단양 밤재	3029
# 충청북도	단양 청년봉	3030
# 충청북도	단양 삼태산	3031
# 충청북도	제천 장석산	3891
# 충청북도	충주 천등산	3892
# 충청북도	음성 원통산	3893
# 충청북도	괴산 박달산	3894
# 충청북도	충주 남산	3895
# 충청북도	단양 도솔봉	3896
# 충청북도	옥천 팔음산	3897
# 충청북도	보은 금단산	3898
# 충청북도	옥천 탑산	3899
# 충청북도	영동 삼봉산	3900
# 충청북도	괴산 대곡산	3901
# 충청북도	단양 태화산	3902
# 충청북도	보은 염동산	3903
# 충청북도	괴산 송인산	3904
# 충청북도	진천 양천산	3905
# 충청북도	진천 만뢰산	3906
# 충청북도	충주 적보산	3910
# 충청북도	청주 오봉산	3911
# 충청북도	청주 불당상봉	3912
# 충청북도	옥천 암산	3913
# 충청북도	옥천 거멍산	3914
# 충청북도	보은 시루산	3915
# 충청북도	옥천 금적산	3916
# 충청북도	보은 삼승산	3917
# 충청북도	보은 노성산	3918



# 전라남도	순천 수이봉	6000
# 전라남도	고흥 두방산	6001
# 전라남도	화순 고비산	6002
# 전라남도	곡성 곤방산	6003
# 전라남도	영광 구수산	6004
# 전라남도	진도 대곡산	6005
# 전라남도	진도 여귀산	6006
# 전라남도	화순 매봉산	6007
# 전라남도	영광 운무산	6008
# 전라남도	장흥 용두산	6009
# 전라남도	장흥 생금산	6010
# 전라남도	순천 망일봉	6011
# 전라남도	순천 까망 몰랑이산	6012
# 전라남도	보성 큰봉	6013
# 전라남도	화순 두봉산	6014
# 전라남도	순천 제석산	6892
# 전라남도	완도 백운봉	6893
# 전라남도	장흥 옥녀봉	6894
# 전라남도	화순 모후산	6895
# 전라남도	장성 방장산	6900
# 전라남도	장성 문수산	6901
# 전라남도	강진 서기산	6902
# 전라남도	해남 달마산	6903
# 전라남도	장흥 가지산	6904
# 전라남도	곡성 봉두산	6905
# 전라남도	구례 솔봉	6906
# 전라남도	여수 봉황산	6907
# 전라남도	보성 제암산	6908
# 전라남도	보성 봉화산	6909
# 전라남도	나주 농암산	6912
# 전라남도	함평 고산봉	6913
# 전라남도	장성 병풍산	6914
# 전라남도	순천 고동산	6915
# 전라남도	화순 용암산	6916
# 전라남도	보성 초암산	6917
# 전라남도	보성 천봉산	6918
# 전라남도	광양 백운산(노랭이봉)	6919



# 전라북도	무주 청량산	5890
# 전라북도	진안 고산	5891
# 전라북도	순창 추령봉	5899
# 전라북도	완주 시루봉	5900
# 전라북도	완주 실내봉	5901
# 전라북도	완주 운장산	5902
# 전라북도	완주 국사봉	5903
# 전라북도	완주 남당산	5904
# 전라북도	임실 지초봉	5905
# 전라북도	장수 할미봉	5906
# 전라북도	진안 성수산	5907
# 전라북도	무주 민주지산	5908
# 전라북도	무주 조항산	5909
# 전라북도	무주 덕유산	5910
# 전라북도	장수 장안산	5911
# 전라북도	남원 봉화산	5912
# 전라북도	진안 덕태산	5913
# 전라북도	진안 내동산	5914
# 전라북도	정읍 상두산	5915
# 전라북도	정읍 회문산	5916
# 전라북도	순창 여분산	5917
# 전라북도	순창 추월산	5918
# 전라북도	고창 방장산(솔재)	5919



# 경상남도	거제 북병산	8000
# 경상남도	통영 도덕산	8001
# 경상남도	거창 기백산	8002
# 경상남도	거제 노자산	8003
# 경상남도	산청 철마산	8004
# 경상남도	함양 용추자연휴양림	8005
# 경상남도	함양 대봉산	8006
# 경상남도	거창 수망령	8007
# 경상남도	거창 금원산자연휴양림	8008
# 경상남도	거창 중우박골	8009
# 경상남도	고성 갈모봉	8010
# 경상남도	거제 고산자봉	8890
# 경상남도	하동 형제봉	8891
# 경상남도	하동 묵계재	8892
# 경상남도	산청 왕등재	8893
# 경상남도	함양 법화산	8894
# 경상남도	고성 향로봉	8895
# 경상남도	거창 단지봉	8896
# 경상남도	남해 대기봉	8897
# 경상남도	창녕 영취산(병봉)	8898
# 경상남도	양산 영취산(시살등)	8899
# 경상남도	함안 천주산	8901
# 경상남도	사천 실봉산	8902
# 경상남도	산청 둔철산	8903
# 경상남도	의령 한우산	8904
# 경상남도	김해 불모산	8905
# 경상남도	거창 월봉산	8906
# 경상남도	거창 금원산	8907
# 경상남도	산청 황매산	8908
# 경상남도	의령 장등산	8909
# 경상남도	양산 천성산	8911
# 경상남도	양산 대운산	8913
# 경상남도	진주 월아산	8916
# 경상남도	창원 평지산	8917
# 경상남도	함양 삼봉산	8918



# 경상북도	봉화 묘봉	7000
# 경상북도	봉화 미림산	7001
# 경상북도	봉화 가부재	7002
# 경상북도	봉화 문수산	7003
# 경상북도	봉화 옥석산	7004
# 경상북도	봉화 예배령	7005
# 경상북도	봉화 조산봉	7006
# 경상북도	봉화 구룡산	7007
# 경상북도	영주 자구산	7008
# 경상북도	문경 조항령	7009
# 경상북도	상주 기양산	7010
# 경상북도	청송 구암산	7011
# 경상북도	군위 매봉	7012
# 경상북도	김천 연석봉	7013
# 경상북도	고령 문수봉	7014
# 경상북도	문경 매봉	7015
# 경상북도	영덕 등운산	7016
# 경상북도	영덕 바데산	7017
# 경상북도	영양 금장산	7018
# 경상북도	청송 면봉산	7019
# 경상북도	김천 송곡령	7020
# 경상북도	상주 백화산	7021
# 경상북도	김천 월매산	7022
# 경상북도	울진 진조산	7023
# 경상북도	울진 대령산	7024
# 경상북도	봉화 늦재	7025
# 경상북도	봉화 비룡산	7026
# 경상북도	봉화 횡악산	7027
# 경상북도	봉화 죽미산	7028
# 경상북도	영주 흰봉산	7029
# 경상북도	울진 오미산	7030
# 경상북도	영덕 대봉산	7031
# 경상북도	영덕 칠보산	7032
# 경상북도	영양 조비산	7033
# 경상북도	영양 추령	7034
# 경상북도	봉화 청옥산	7891
# 경상북도	봉화 큰재	7892
# 경상북도	울진 통고산	7893
# 경상북도	울진 가재미재	7894
# 경상북도	울진 아구산	7895
# 경상북도	봉화 장군봉	7896
# 경상북도	영양 함박산	7897
# 경상북도	영덕 명동산	7898
# 경상북도	안동 용바위	7899
# 경상북도	청송 감연산	7900
# 경상북도	영덕 독경산	7901
# 경상북도	영덕 삿갓봉	7902
# 경상북도	포항 내연산	7903
# 경상북도	포항 조항산	7904
# 경상북도	의성 주월산	7905
# 경상북도	안동 수운산	7906
# 경상북도	영양 검마산	7907
# 경상북도	예천 가재봉	7908
# 경상북도	울진 백병산전곡리	7909
# 경상북도	성주 박석산	7913
# 경상북도	경산 삼성산	7914
# 경상북도	경산 발백산	7915
# 경상북도	구미 비봉산	7916
# 경상북도	울진 백병산	7917
# 경상북도	영주 용암산(한천시험림)	7918
# 경상북도	영주 천부산	7919



# 제주도	제주 노로오름	9910
# 제주도	제주 사려니숲	9911
# 제주도	서귀포시험림	9912
# 제주도	난대림연구소	9913
# 제주도	제주 들위오름	9914