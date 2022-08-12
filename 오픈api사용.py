# 오픈api사용.py
#라이브러리 import
import requests
import pprint
import json

# url 입력

url = 'http://api.data.go.kr/openapi/tn_pubr_public_cctv_api?serviceKey=개인인증키입력&pageNo=1&numOfRows=10&type=json'

response = requests.get(url)

contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))

## json을 DataFrame으로 변환하기 ##

#문자열을 json으로 변경
json_ob = json.loads(contents)
print(type(json_ob)) #json타입 확인

# 필요한 내용만 꺼내기
body = json_ob['response']['body']['items']
print(body)

# pandas import
import pandas as pd
from pandas.io.json import json_normalize

# Dataframe으로 만들기
dataframe = json_normalize(body)

print(dataframe)