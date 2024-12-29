# todo: 常见的浏览器操作
#
# @Time: 2024/12/29 12:50:42
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获取当前页面的标题
print(driver.title)
# 获取当前页面的url
print(driver.current_url)
# 获取当前页面的源码的长度
print(len(driver.page_source))

time.sleep(3)

# 最大化浏览器窗口
driver.maximize_window()
time.sleep(3)

# 设置浏览器窗口的大小
driver.set_window_size(800, 600)
time.sleep(3)

# 调转到新的页面
driver.get("http://www.douban.com")
time.sleep(3)

# 后退
driver.back()
time.sleep(3)

# 刷新
driver.refresh()
time.sleep(3)

# 前进
driver.forward()
time.sleep(3)

# 保存当前页面快照
driver.save_screenshot("./images/screemshot.png")

# 关闭当前标签页
driver.close()

# 关闭浏览器，退出进程
driver.quit()
