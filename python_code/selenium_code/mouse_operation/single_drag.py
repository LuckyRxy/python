# todo: 鼠标单元素拖动
#
# @Time: 2024/12/29 14:38:54
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 启动浏览器
driver = webdriver.Chrome()

# 打开一个页面（这里使用一个简单的拖动示例）
driver.get("https://www.selenium.dev/selenium/web/webdriver.html")

# 等待页面加载
time.sleep(2)

# 找到可拖动的元素
draggable_element = driver.find_element(By.CSS_SELECTOR, ".drag-box")

# 创建 ActionChains 对象
action = ActionChains(driver)

# 获取元素的位置
location = draggable_element.location
x_offset = location['x']  # 获取元素的 X 坐标
y_offset = location['y']  # 获取元素的 Y 坐标

# 模拟拖动元素
# 点击并按住，然后向右下方移动 100 像素（可以根据需要调整偏移量）
# release()：释放鼠标
action.click_and_hold(draggable_element).move_by_offset(100, 100).release().perform()

# 等待查看结果
time.sleep(5)

# 关闭浏览器
driver.quit()
