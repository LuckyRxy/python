# todo: 使用name选择器定位元素
#
# @Time: 2024/12/29 09:40:39
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element(by=By.NAME, value="wd").send_keys("selenium")
driver.find_element(by=By.ID, value="su").click()

time.sleep(5)
driver.quit()