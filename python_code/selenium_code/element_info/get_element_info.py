# todo: 获取元素信息
# 三个方法可以获取元素信息：is_displayed()、is_enabled()、is_selected()，分别用于判断元素是否可见、是否可用、是否被选中。
# @Time: 2024/12/29 13:15:00
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_input_text")

# 等待iframe加载并切换到iframe
wait = WebDriverWait(driver, 10)
iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe")))
driver.switch_to.frame(iframe)

# 等待输入框加载并获取大小
input_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/input[1]")))
size = input_element.size

# 获取标签中的内容
text = driver.find_element(By.XPATH, "/html/body/p[1]").text

# 切换回主文档
driver.switch_to.default_content()

# 获取超链接的链接地址（修正herf为href）
address = driver.find_element(By.XPATH, "//*[@id='tiy_btn_index']/a").get_attribute("href")

print("{},{},{}".format(size, text, address))

# 切换回主文档
driver.switch_to.default_content()

driver.quit()





