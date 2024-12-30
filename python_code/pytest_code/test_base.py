# todo: pytest base operation
# 模块（.py）和方法名以 test_ 开头，类名以 Test 开头，不能有 __init__ 方法
# 结合allure生成测试报告 （在电脑先安装allure，之后在虚拟环境中安装allure-pytest）
#       pytest --alluredir=./allure-results
#       allure serve ./allure-results
# 
# @Time: 2024/12/30 10:01:24
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import pytest

class TestDemo1:

    def test_one(self):
        print("test_one")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("test_two")
        x = "hello"
        assert hasattr(x, 'check')

# 建议使用命令行方式进行执行
if __name__ == '__main__':
    pytest.main()