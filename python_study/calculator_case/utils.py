# todo: 封装浏览器驱动对象
#
# @Time: 2024/12/30 15:36:58
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

from selenium import webdriver

class DriverUtils:
    
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None