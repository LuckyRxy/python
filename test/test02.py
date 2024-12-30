# todo: 测试selenium的窗口截图
#
# @Time: 2024/12/29 20:25:31
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
from selenium import webdriver

def test_screenshot():

    driver = webdriver.Chrome()

    driver.get("https://www.baidu.com")

    driver.save_screenshot("./baidu1.png")
    driver.get_screenshot_as_file("./baidu2.png")

    driver.quit()

if __name__ == "__main__":
    test_screenshot()
