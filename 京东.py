from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get(r"https://www.jd.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@type='text']").send_keys("电动牙刷")
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
sleep(1)
print(driver.title)
ele = driver.window_handles
print(ele)
driver._switch_to.window(ele[-1])
sleep(1)
print(driver.title)
driver.find_element_by_xpath("//*[@data-sku='100014962608']").click()
