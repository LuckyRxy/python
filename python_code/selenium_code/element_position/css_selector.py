# todo: 使用css选择器定位元素
#
# @Time: 2024/12/29 09:52:32
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element(by=By.CSS_SELECTOR, value="#kw").send_keys("selenium")
driver.find_element(by=By.CSS_SELECTOR, value="#su").click()

time.sleep(5)
driver.quit()

