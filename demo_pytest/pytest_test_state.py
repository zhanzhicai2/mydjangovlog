import pytest
# @pytest.fixture()
# def func():
#     print("获取用户名")
#     a = "yygirl"
#     assert a == "yygirl123"
#     return a
#
# def test_func(func):
#     assert user == "yygirl"

@pytest.fixture()
def func():
    print("获取密码")
    a = "polo"
    return a

def test_func(func):
    raise NameError
    assert func == "polo"