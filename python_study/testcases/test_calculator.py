# todo: calculator testcases
#
# @Time: 2024/12/30 16:07:08
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import sys

import pytest
from calculator_case.utils import DriverUtils
from calculator_case.calculator_service import CalculatorService
from calculator_case.build_data import build_data



class TestCalculator:

    def setup_class(self):
        self.driver = DriverUtils.get_driver()
        self.CalculatorService = CalculatorService()
    
    def teardown_class(self):
        DriverUtils.quit_driver()

    @pytest.mark.parametrize("num1, num2, expect", build_data())
    def test_add(self, num1, num2, expect):
        print("num1:{}, num2:{}, expect:{}", num1, num2, expect)
        pass

    def test_sub(self):
        pass

    def test_mul(self):
        pass

    def test_div(self):
        pass

if __name__ == "__main__":
    pytest.main()
