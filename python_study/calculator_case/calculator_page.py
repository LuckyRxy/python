# todo: 封装计算机页面对象
#
# @Time: 2024/12/30 15:39:11
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

from selenium.webdriver.common.by import By
from utils import DriverUtils

class CalculatorPage:
    
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.driver.get("http://cal.apple886.com/")
        self.driver.implicitly_wait(10)

        self.digital_button = (By.ID, "simple{}")
        self.add_button = (By.ID, "simpleAdd")
        self.eq_button = (By.ID, "simpleEqual")
        self.result = (By.ID, "resultIpt")

    def find_digital_button(self, num):
        return self.driver.find_element(self.digital_button[0], self.digital_button[1].format(num))

    def find_add_button(self):
        return self.driver.find_element(self.add_button[0], self.add_button[1])

    def find_eq_button(self):
        return self.driver.find_element(self.eq_button[0], self.eq_button[1])
    
    def find_result(self):
        return self.driver.find_element(self.result[0], self.result[1])