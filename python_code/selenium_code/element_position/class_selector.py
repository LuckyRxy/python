# todo: 使用class选择器定位元素
#
# @Time: 2024/12/29 09:42:49
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element(by=By.CLASS_NAME, value="s_ipt").send_keys("selenium")
driver.find_element(by=By.CLASS_NAME, value="s_btn").click()

time.sleep(5)
driver.quit()