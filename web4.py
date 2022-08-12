# web4.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

#이 부분을 수정한다. 
driver = set_chrome_driver()
driver.implicitly_wait(3)
#driver.get('https://google.com')
driver.get('https://nid.naver.com/nidlogin.login')

#아래의 코드도 수정됨 
userID = driver.find_elements(By.ID, 'id')[0]
userPwd = driver.find_elements(By.ID, 'pw')[0]
userID.send_keys("kim")
userPwd.send_keys("1234")

#로그인버튼 클릭 
# btn = driver.find_elements(By.ID, 'log.login')
# btn.click() 
