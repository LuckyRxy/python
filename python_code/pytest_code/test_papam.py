# todo: pytest参数化
#
# @Time: 2024/12/30 14:33:58
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import pytest

class TestParam:

    def ad(self, a, b):
        return a + b

    @pytest.mark.parametrize("num1, num2, expected", [(2, 8, 10), (4, 6, 10), (5, 5, 11)])
    def test_eval(self, num1, num2, expected):
        assert self.ad(num1, num2) == expected