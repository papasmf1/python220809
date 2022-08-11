# db1.py
import sqlite3
#연결객체 생성
con = sqlite3.connect(":memory:")
#커서객체 생성
cur = con.cursor()
#테이블 구조(테이블 스키마 생성)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 레코드(행)을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

