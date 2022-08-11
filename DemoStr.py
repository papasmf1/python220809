# DemoStr.py
strA = "python is very powerful"
strB = "파이썬은 강력해"
print( len(strA) )
print( len(strB) )
print( strA.capitalize() )
print( strA.count("p") )
print( strA.count("p", 7) )
print( strA.startswith("py") )
print( strA.endswith("ful") )

print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

#문자열 전처리(데이터)
strC = "<<< spam and ham >>>"
result = strC.strip("<> ")
print(strC)
print(result)

print("---치환---")
result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print("---다시 합치기---")
print( ":)".join(lst) )
