# todo: 使用xpath选择器定位元素
#
# @Time: 2024/12/29 10:10:40
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element(by=By.XPATH, value="//*[@id='kw']").send_keys("selenium")
driver.find_element(by=By.XPATH, value="//*[@id='su']").click()

time.sleep(5)
driver.quit()
