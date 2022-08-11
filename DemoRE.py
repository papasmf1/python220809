# DemoRE.py
import re 

result = re.search("[0-9]*th", "  35th")
print( result )
print( result.group() )

# result = re.match("[0-9]*th", "  35th")
# print( result )
# print( result.group() )

print( bool(re.search("apple", "this is apple")) )
print( bool(re.match("apple", "apple")) )
print( bool(re.search("\d{4}", "올해는 2022년입니다.")) )
print( bool(re.search("\d{5}", "우리동네는 52300")) )

result = re.search("\d{5}", "우리동네는 52300")
print( result.group() )

strA = "python::is::very::powerful"
lst = strA.split("::")
print(lst)
print(len(lst))

#전화번호
telChecker = re.compile("(\d{2,3})-(\d{3,4})-(\d{4})")
result = telChecker.match("02-3429-5000")
print(result.group())
print(result.group(1))
print(result.group(2))
