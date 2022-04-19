
import pytest

def setup_module():
    print("====整个.py模块开始前执行一次：打开浏览器===")
def deardown_module():
    print("====整个.py模块结束后只执行一次：关闭浏览器===")


def setup_function():
    print("====每个函数级别用例开始前执行setup_function===")
def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function===")


# 函数
def test_function_one():
    print("function_one")


def test_function_two():
    print("function_two")


#类级别用例
class TestCase():
    def setup_class(self):
        print("===整个测试类开始前执行一次setup_class====")
    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class===")

    # 类方法
    def setup_method(self):
        print("===类里面每个测试用例前都会执行一次setup_method===")
    def teardown_method(self):
        print("===类里面的每测试用例结束后执行一次teardown_method====")

    def setup(self):
        print("=类里面每个测试用例执行前都会执行setup=")
    def teardown(self):
        print("=类里面每个用例结束都会执行teardown=")

    def setup(self):
        print("=类里面每个用例执行前都会执行setup=")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=")

    def test_mothod_three(self):
        print("three")
    def test_mothod_four(self):
        print("four")

#
if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "pytest_test_setup_teardown.py"])
#     # pytest.main(["-q", "pytest_test_srtup_teardown.py"])
