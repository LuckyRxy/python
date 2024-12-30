# todo: 操作下拉框
#
# @Time: 2024/12/29 17:00:40
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 启动浏览器
driver = webdriver.Chrome()

driver.get('https://www.bootstrap.cn/doc/read/125.html')

# 定位下拉框元素
dropdown = Select(driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[1]/select'))

# 通过索引选择（索引从0开始）
dropdown.select_by_index(1)
time.sleep(3)

# 通过value属性值选择
dropdown.select_by_value('2')
time.sleep(3)

# 通过显示文本选择
dropdown.select_by_visible_text('Three')
time.sleep(3)

# 关闭浏览器
driver.quit()
