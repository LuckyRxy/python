# todo: 操作iframe
#
# @Time: 2024/12/29 20:00:07
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

# 获取标签中的内容
text = driver.find_element(By.XPATH, "/html/body/p[1]").text

# 切换回主文档
driver.switch_to.default_content()

# 获取超链接的链接地址（修正herf为href）
address = driver.find_element(By.XPATH, "//*[@id='tiy_btn_index']/a").get_attribute("href")

print("{},{}".format(text, address))

# 切换回主文档
driver.switch_to.default_content()

driver.quit()