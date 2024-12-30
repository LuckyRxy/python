# todo: 计算机页面操作类（层）
#
# @Time: 2024/12/30 15:50:28
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

from calculator_page import CalculatorPage

class CalculatorHandle:
    
    def __init__(self):
        self.calculator_page = CalculatorPage()

    def click_digital(self, num):
        self.calculator_page.find_digital_button(num).click()

    def click_add(self):
        self.calculator_page.find_add_button().click()

    def click_eq(self):
        self.calculator_page.find_eq_button().click()

    def get_result(self):
        return self.calculator_page.find_result().get_attribute("value")
    
    def input_numbers(self, nums):
        for num in nums:
            self.click_digital(num)