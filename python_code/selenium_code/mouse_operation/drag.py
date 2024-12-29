# todo: 模拟鼠标拖动操作
#
# @Time: 2024/12/29 14:27:13
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 启动浏览器
driver = webdriver.Chrome()

# 打开一个测试页面（例如拖放的示例页面）
driver.get("https://www.dhtmlx.com/docs/products/dhtmlxTree/")

# 等待页面加载完成（你可以使用 WebDriverWait 来显式等待）
time.sleep(2)

# 找到要拖动的源元素
source = driver.find_element(By.XPATH, "//span[text()='Item 1']")

# 找到目标元素（你要把源元素拖到这个位置）
target = driver.find_element(By.XPATH, "//span[text()='Item 2']")

# 创建 ActionChains 对象
action = ActionChains(driver)

# 模拟鼠标拖动操作：按住源元素并拖动到目标元素
action.drag_and_drop(source, target).perform()

# 等待 5 秒查看结果
time.sleep(5)

# 关闭浏览器
driver.quit()
