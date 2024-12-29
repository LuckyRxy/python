# todo: 模拟键盘操作(还有一些其它的操作，请自行查找)
#
# @Time: 2024/12/29 14:47:20
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 显式等待，确保输入框已经加载并且可见
wait = WebDriverWait(driver, 10)
input_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#kw")))

# 模拟键盘操作
input_box = driver.find_element(By.ID, "kw")
input_box.send_keys("selenium")
# time.sleep(5)

# 删除一个字符
input_box.send_keys(Keys.BACK_SPACE)

# 全选输入框内容
input_box.send_keys(Keys.CONTROL, 'a')

time.sleep(5)

driver.quit()