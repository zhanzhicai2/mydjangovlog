import pytest

@pytest.mark.weibo
def test_weibo():
    print("测试微博")


# @pytest.mark.xfail()
# def test_case1():
#     a = "a"
#     b = "b"
#     assert a != b

@pytest.mark.toutiao
def test_toutiao():
    print("测试头条")

@pytest.mark.toutiao
def test_toutiao2():
    print("再次测试头条")

@pytest.mark.xinlang
class TestClass:
    def test_xinlang(self):
        print("测试新浪")

def testnoMark():
    print("没有自定义标记")