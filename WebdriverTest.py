from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path="./chromedriver.exe"
)

url = "https://www.instagram.com/explore/tags/sportscar/"
driver.get(url) #Enter치는 효과
time.sleep(5)
pageString = driver.page_source
print(pageString)
#인스타 껍데기
#인스타 내용

driver.close()