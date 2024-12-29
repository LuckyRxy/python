# todo: 模拟鼠标右键操作
#
# @Time: 2024/12/29 13:50:57
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 创建鼠标对象
action = ActionChains(driver)
# 调用鼠标右键点击方法
action.context_click(driver.find_element(By.CSS_SELECTOR, value="#su"))
# 调用鼠标执行方法
action.perform()

time.sleep(5)

driver.close()
driver.quit()
