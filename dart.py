from selenium import webdriver
import time

rootPath ='.'
driver = webdriver.Chrome(
    executable_path="{}/chromedriver.exe".format(rootPath)
)

url = "https://dart.fss.or.kr"
driver.get(url)

# driver.find_element_by_class_name()
driver.find_element_by_xpath('//*[@id="textCrpNm"]').send_keys("셀트리온")
driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/p[4]/input').click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="checkCorpSelect"]').click()
driver.find_element_by_xpath('//*[@id="corpListContents"]/div/fieldset/div[3]/a[1]/img').click()

driver.find_element_by_xpath('//*[@id="searchpng"]').click()

pageContent = driver.page_source
print(pageContent)

time.sleep(10)
print("Data collection done!!!")
driver.close()
# //*[@id="checkCorpSelect"]
# //*[@id="corpListContents"]/div/fieldset/div[3]/a[1]/img