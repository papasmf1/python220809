# DemoFile.py

strURL = "http://ycampus.com/?page=" + str(1) 
print(strURL)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---정렬방식지정---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(5))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(5))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(5/3))
print("{0:.3f}".format(5/3))

#numpy
import math 
print("item:{0}".format(math.ceil(3.14)))
print("item:{0}".format(math.floor(3.14)))