# 为了提高复用性，我们在写测试用例的时候，会用到不同的fixture，比如：最常见的登录操作，大部分的用例的前置条件都是登录
# 假设不同的用例想登录不同的测试账号，那么登录fixture就不能把账号写死，需要通过传参的方式来完成登录操作
import pytest


# @pytest.fixture()
# def login(request):
#     name = request.param
#     print(f'==账号是{name}==')
#     return name
@pytest.fixture()
def login(request):
    name = request.param
    print(f'==账号是{name}==')
    return name


data_1 = ["pdd","ddd"]
ids = [f'login_test_name is:{name}'for name in data_1]


@pytest.mark.parametrize("login",data_1,ids=ids,indirect=True)
def test_name(login):
    print(f'测试用例的登录账号是：{login}')

#案例二：多个参数
data_2 = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
]

@pytest.fixture()
def login_2(request):
    param =request.param
    print(f"账号是{param['username']},密码是{param['pwd']}")
    return param


@pytest.mark.parametrize('login_2',data_2,indirect=True)
def test_name_pwd(login_2):
    print(f"账号是{login_2['username']},密码是{login_2['pwd']}")


#案例三：多个fixture（只加一个装饰器

data_3 = [
    ("name","psw1"),
    ("name2", "pwd2")
]
@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print(f"登录账号{user}")
    return user

@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print(f"登录密码{psw}")
    return psw

@pytest.mark.parametrize("input_user,input_psw",data_3,indirect=True)
def test_more_fixture(input_user,input_psw):
    print("fixture返回的内容：",input_user,input_psw)