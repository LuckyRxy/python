# todo: 模拟鼠标双击操作
#
# @Time: 2024/12/29 14:06:03
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动浏览器
driver = webdriver.Chrome()

# 打开百度首页
driver.get("http://www.baidu.com")

# 显式等待，确保输入框已经加载并且可见
wait = WebDriverWait(driver, 10)
input_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#kw")))

# 在输入框中输入“你好”
input_box.send_keys("你好")

# 使用 ActionChains 模拟双击操作
action = ActionChains(driver)
action.double_click(input_box).perform()

# 等待 5 秒查看结果
time.sleep(5)

# 关闭浏览器
driver.quit()
