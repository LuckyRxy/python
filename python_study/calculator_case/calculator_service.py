# todo: 计算机操作业务类（层）
#
# @Time: 2024/12/30 15:54:42
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

from calculator_handle import CalculatorHandle

class CalculatorService:
    
    def __init__(self):
        self.calculator_handle = CalculatorHandle()
    
    def add(self, num1, num2):
        self.calculator_handle.input_numbers(str(num1))
        self.calculator_handle.click_add()
        self.calculator_handle.input_numbers(str(num2))
        self.calculator_handle.click_eq()
        return self.calculator_handle.get_result()
    
    # def sub(self, num1, num2):
    #     self.calculator_handle.input_numbers([num1, num2])
    #     self.calculator_handle.click_sub()
    #     self.calculator_handle.click_eq()
    #     return self.calculator_handle.get_result()
    
    # def mul(self, num1, num2):
    #     self.calculator_handle.input_numbers([num1, num2])
    #     self.calculator_handle.click_mul()
    #     self.calculator_handle.click_eq()
    #     return self.calculator_handle.get_result()
    
    # def div(self, num1, num2):
    #     self.calculator_handle.input_numbers([num1, num2])
    #     self.calculator_handle.click_div()
    #     self.calculator_handle.click_eq()
    #     return self.calculator_handle.get_result()