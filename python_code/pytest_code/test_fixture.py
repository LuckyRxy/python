# todo: 测试fixture
#
# @Time: 2024/12/30 13:09:51
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import pytest


"""
@todo: 简单测试
@return: 
"""
@pytest.fixture()
def simple_fixture():
    return 404

@pytest.mark.skip()
def test_fixture(simple_fixture):
    assert simple_fixture == 404


"""
@todo: 使用不同作用域的 fixture, module：模块级别，在整个模块中只运行一次
@return: 
"""
@pytest.fixture(scope='module')
def resource():
    print("Initializing resource...")
    return "Shared resource"

def test_case_1(resource):
    print("Running test_case_1")
    assert resource == "Shared resource"

def test_case_2(resource):
    print("Running test_case_2")
    assert resource == "Shared resource"

"""
@todo: 实现类似 setup 和 teardown 的功能
@return: 
"""
@pytest.fixture()
def resource1():
    print("start resource1")
    yield # 上面的代码相当于 setup，下面的代码相当于 teardown
    print("end resource1")
    return "resource1"

def test_case_3(resource1):
    print("Running test_case_3")
    assert resource1 == "resource1"

def test_case_4(resource1):
    print("Running test_case_4")
    assert resource1 == "resource1"

