# DemoOS.py
from os.path import *

print( abspath("python.exe") )
print( basename("c:\\work\\demo.py") )
print( getsize("c:\\python39\\python.exe") )

from os import * 
#system("notepad.exe")
print("운영체제이름:", name)

#파일 목록 
import glob 
result = glob.glob("c:\\work\\*.py")
print(result)

