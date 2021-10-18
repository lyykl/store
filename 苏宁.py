from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.suning.com")

driver.find_element_by_xpath("//*[@class='search-keyword']").send_keys("华为Mate40")

driver.find_element_by_xpath("//*[@class='search-btn btn-new']").click()

driver.find_element_by_xpath("//*[@tempindex='02']").click()
# driver.find_element_by_xpath("//*[@name='item_12199717163_ysys_size01']").click()
# driver.find_element_by_xpath("//*[@class='selected']").click()
sleep(5)
print(driver.title)
ele = driver.window_handles
print(ele)
driver._switch_to.window(ele[-1])
sleep(5)
print(driver.title)
driver.find_element_by_xpath("//*[@id='addCart']").click()

