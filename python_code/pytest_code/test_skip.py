# todo: 测试跳过
#
# @Time: 2024/12/30 12:05:23
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import pytest

class TestSkip:

    workage = 17
    
    def test_skip(self):
        print("no skip")
        assert 1 == 1

    @pytest.mark.skip(reason="skip test without condition")
    def test_skip_mark(self):
        print("test_skip_mark")
        assert 1 == 1

    @pytest.mark.skipif(workage < 18, reason="skip test with condition")
    def test_skip_mark_if(self):
        print("test_skip_mark_if")
        assert 1 == 1

    