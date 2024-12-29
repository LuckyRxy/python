# todo: 模拟鼠标悬停操作
#
# @Time: 2024/12/29 14:33:46
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 启动浏览器
driver = webdriver.Chrome()

# 打开页面
driver.get("https://www.baidu.com")

# 等待页面加载完成
time.sleep(2)

# 找到要悬停的父元素（如设置按钮）
element_to_hover = driver.find_element(By.CSS_SELECTOR, "#s-usersetting-top")

# 悬停并点击下拉菜单中的一个选项
action = ActionChains(driver)
action.move_to_element(element_to_hover).perform()

# 找到下拉菜单中的一个元素并点击
menu_option = driver.find_element(By.XPATH, "//*[text()='搜索设置']")
menu_option.click()

# 等待 5 秒查看效果
time.sleep(5)

# 关闭浏览器
driver.quit()

