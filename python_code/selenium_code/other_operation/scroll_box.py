# todo: 滚动操作
#
# @Time: 2024/12/29 19:17:26
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3school.com.cn/index.html")

# 滚动到底部
js = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(3)

# 滚动到顶部
js = "window.scrollTo(0, 0)"
driver.execute_script(js)
time.sleep(3)

# 滚动到指定元素
element = driver.find_element(By.XPATH, '//*[@id="navsecond"]/ul[4]/li[1]/a')
js = "arguments[0].scrollIntoView();"
driver.execute_script(js, element)
time.sleep(3)

driver.quit()
