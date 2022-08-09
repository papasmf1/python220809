# DemoDict.py
#딕셔너리(dict)
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print( len(device) )
print( device["아이폰"] )
#print( device[0] )
#입력
device["맥북"] = 20
#수정
device["아이폰"] = 6 
#삭제
del device["아이폰"]

for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)

for k in device.keys():
    print(k)

for v in device.values():
    print(v)

#전화번호 관리
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print( "kim" in phone )
print( "kang" not in phone )

#참조를 복사
p = phone 
p["kang"] = "1234"
print(id(phone), id(p))
print(phone)
print(p)

