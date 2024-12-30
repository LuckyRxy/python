# todo: 操作cookie
#
# @Time: 2024/12/30 09:04:55
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.taobao.com")

# 获取所有的cookie
cookies = driver.get_cookies()
print(cookies)

driver.quit()

driver = webdriver.Chrome()
# 访问淘宝购物车
driver.get(r"https://cart.taobao.com/cart.htm")
time.sleep(5)

# 添加cookie
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(5)

driver.quit()