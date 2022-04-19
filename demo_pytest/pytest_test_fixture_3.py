import pytest

@pytest.fixture(scope="session")
def open():
    # 会话前置操作setup
    print("===打开浏览器===")
    test = "测试变量是否返回"
    yield test
    # 会话后置操作teardown
    print("===关闭浏览器===")

@pytest.fixture
def login(open):
    # 方法级别前置操作setup
    print(f"输入账号，密码先登录{open}")
    name = "==我的账号=="
    pwd = "==我的密码=="
    age = "==我的年龄=="
    # 返回变量
    yield name, pwd,age
    # 方法界别后置teardown
    print("登录成功")

def test_s1(login):
    print("==用例1==")
    print(login)
    # 分别赋值给不同变量
    name,pwd,age = login
    print(name,pwd,age)
    assert"==我的账号==" == name
    assert"==我的密码==" == pwd
    assert"==我的年龄==" == age

def test_s2(login):
    print("==用例2==")
    print(login)

