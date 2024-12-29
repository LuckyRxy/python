# todo: 获取元素信息
#
# @Time: 2024/12/29 13:15:00
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.maximize_window()

driver.get("https://www.baidu.com")

# 获取输入框的大小
size = driver.find_element(By.CSS_SELECTOR, value="#kw").size
# 获取标签中的内容
selector_info = r"//*[@id='title-content']/span[1]"
text = driver.find_element(By.XPATH, value=selector_info).text
# 获取超链接的链接地址
selector_info = r"#title-content"
address = driver.find_element(By.XPATH, value=selector_info).get_attribute("herf")

print("{},{},{}".format(size, text, address))

time.sleep(5)

driver.close()
driver.quit()


