import pytest
import sys
# 标记

skipmark = pytest.mark.skip(reason="不能在window上运行=====")
skipifmark = pytest.mark.skipif(sys.platform == 'win32', reason="不能在window上运行啦啦啦=====")

# if sys.platform.startswith("win"):
#     pytest.skip("skipping windows-only tests",allow_module_level=True)


@pytest.fixture(autouse=True)
def login():
    print("===登录===")


def test_case01():
    print("我的测试用例1111")


@pytest.mark.skip(reason="不执行该用例！！因为没有写好！！")
def test_case02():
    print("我是测试用例2222")


class Test1:
    def test_1(self):
        print("%%我是类测试用例1111%%")

    @pytest.mark.skip(reason="不想执行")
    def test_2(self):
        print("%%我是类测试用例2222%%")


@pytest.mark.skip(reason="类也可以跳过不执行")
class TestSkip:
    def test_1(self):
        print("%%不会执行%%")


def test_function():
    n = 1
    while True:
        print(f"这是我的第{n}条用例")
        n +=1
        if n == 5:
            pytest.skip("我已经跑五次了不跑了")


@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
class TestSkipIf(object):
    def test_function(self):
        print("不能在window上运行")

@skipmark
class TestSkip_Mark(object):

    @skipifmark
    def test_function(self):
        print("测试标记")

    def test_def(self):
        print("测试标记")


@skipmark
def test_skip():
    print("测试标记")