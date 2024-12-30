# todo: 多窗口操作
#
# @Time: 2024/12/29 20:08:41
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
print("主窗口标题:", driver.title)

# 获取当前窗口句柄
main_window_handle = driver.current_window_handle

# 打开新窗口
driver.execute_script("window.open('https://www.douban.com');")
time.sleep(2)

# 获取所有窗口句柄
all_handles = driver.window_handles
print("所有窗口句柄:", all_handles)

# 切换到新窗口
for handle in all_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)
        break

print("新窗口标题:", driver.title)

time.sleep(3)

# 关闭新窗口
driver.close()

# 切换到主窗口
driver.switch_to.window(main_window_handle)
print("主窗口标题:", driver.title)

time.sleep(3)

driver.quit()