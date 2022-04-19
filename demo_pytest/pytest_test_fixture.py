import pytest

#调用方式fixture
@pytest.fixture
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("测试用例1：登录之后其他动作 111")
def test_s2(): #不传login
    print("测试用例2：不需要登录，操作 222")

# 调用方式二 fixture 装饰器

@pytest.fixture
def login2():
    print("测试用例11：登录之后其他动作 111")
@pytest.mark.usefixtures("login2", "login")
def test_s11():
    print("用例 11：登录之后其它动作 111")
#调用方式三
@pytest.fixture(autouse=True)
def login3():
    print("====auto===")

# 不是test开头，加入装饰器也不会执行fixtrue
@pytest.mark.usefixtures("login2")
def loginss():
    print("123")
