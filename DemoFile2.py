# DemoFile2.py

#파일쓰기
#f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
#raw string notation(r)
#f = open(r"c:\work\test2.txt", "wt", encoding="utf-8")
#linu, unix
f = open("c:/work/test3.txt", "wt", encoding="utf-8")

f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일읽기
f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
print( f.read() )
print( f.tell() )
print("---바이트---")
print(len("첫번째\n두번째\n세번째\n".encode()))

#다시 처음으로 돌아가기
f.seek(0)
lst = f.readlines()
print(lst)
#다시 처음으로 돌아가기
f.seek(0)
print("---한줄씩---")
print( f.readline(), end="" )
print( f.readline(), end="" )
f.close() 

f = open("c:\\work\\test2.txt", "wt")
f.write("hello python is powerful")
f.close() 
f = open("c:\\work\\test2.txt", "rt")
print( f.read(5) )
print( f.tell() )
print( f.read(7) )
print( f.tell() )