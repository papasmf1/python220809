# db1.py
import sqlite3
#연결객체 생성(물리적인 파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체 생성
cur = con.cursor()
#테이블 구조(테이블 스키마 생성)
cur.execute("create table PhoneBook (Name str, PhoneNum str);")

#입력 파라메터 처리(웹페이지, 모바일앱)
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber) )

#1건 레코드(행)을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#작업을 정상적으로 완료(입력, 수정, 삭제)
con.commit() 

