from selenium import webdriver

rootPath ='.'
driver = webdriver.Chrome(
    executable_path="{}/chromedriver.exe".format(rootPath)
)

url = "https://www.facebook.com/"
driver.get(url)

driver.find_element_by_id("email").send_keys("cypaul85@hotmail.com")
# driver.find_element_by_id("pass").send_keys("poweron1#")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("123456")
driver.find_element_by_id("u_0_2").click()