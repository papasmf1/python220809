# DemoTuple2.py 
#튜플을 사용하는 경우
def calc(a,b):
    return a+b, a*b

#첫열로 나와서 
result = calc(3,4)
print(result)
print(result[0])
print(result[1])

#여러개의 인자를 넘기는 경우
print("id:%s, name:%s" % ("kim","김유신"))

#set형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print( type(b) )
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )

#형식을 변경
a = set((1,2,3))
print(a)
print(type(a))
b = list(a)
print(b)
b.append(4)
print(b)
#반복구문
#디버깅할 때 중단점 추가(Break Point)
for item in b:
    print(item)








