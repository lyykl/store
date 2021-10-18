from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"http://8.129.91.152:8765/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/span[1]/a").click()
driver.find_element_by_xpath("//*[@id='phone']").send_keys("15621565365")
time.sleep(15)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("ykl518323")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
driver.switch_to.alert.accept()
driver.find_element_by_xpath("//*[@id='layui-layer2']/div[3]/a[1]").click()
