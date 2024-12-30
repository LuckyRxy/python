import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# 启动浏览器
driver = webdriver.Chrome()


"""
@todo: alert弹窗
@param: 
@return: 
"""
# driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

# # 点击按钮弹出Alert
# driver.switch_to.frame("iframeResult")  # 切换到iframe
# driver.find_element(By.XPATH, "/html/body/button").click()

# time.sleep(3)

# # 切换到Alert并接受
# alert = Alert(driver)
# alert.accept()  # 点击 "OK" 按钮

# time.sleep(3)
# # 关闭浏览器
# driver.quit()

"""
@todo: confirm弹窗
@param: 
@return: 
"""
# driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm")
# driver.switch_to.frame("iframeResult")  # 切换到iframe
# driver.find_element(By.XPATH, "/html/body/button").click()

# time.sleep(3)

# # 切换到Alert并接受
# alert = Alert(driver)
# alert.dismiss()  # 点击 "Cancel" 按钮
# time.sleep(3)
# # 关闭浏览器
# driver.quit()

"""
@todo: prompt弹窗
@param: 
@return: 
"""
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
driver.switch_to.frame("iframeResult")  # 切换到iframe
driver.find_element(By.XPATH, "/html/body/button").click()

time.sleep(3)

# 切换到Alert并接受
alert = Alert(driver)
alert.send_keys("selenium")  # 点击 "Cancel" 按钮
alert.accept()  # 点击 "OK" 按钮
time.sleep(3)
# 关闭浏览器
driver.quit()