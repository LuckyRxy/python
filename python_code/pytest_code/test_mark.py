# todo: 测试标记
#
# @Time: 2024/12/30 11:38:40
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import pytest

class TestMark:
    
    @pytest.mark.user_manager
    def test_demo1(self):
        print("user1")
        pass
    
    @pytest.mark.product_manager
    def test_demo2(self):
        print("product")
        pass

    @pytest.mark.user_manager
    def test_demo3(self):
        print("user2")
        pass

if __name__ == "__main__":
    pytest.main(["-m", "user_manager"])  # 只执行标记为user_manager的用例
