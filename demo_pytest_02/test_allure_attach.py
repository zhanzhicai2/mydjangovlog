import allure
import pytest


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('在fixture前置操作里面添加一个附件txt', 'fixture前置附件', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)

@allure.description("""
这是一个@allure.description装饰器
没有特别的用处
""")
def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    pass

@allure.description_html("""
<h1>Test with some complicated html description</h1>
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  <tr align="center">
    <td>William</td>
    <td>Smith</td>
</table>
""")
def test_multiple_attachments():
    allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
    # allure.attach.file('./reports.html', attachment_type=allure.attachment_type.HTML)


@allure.title("前置操作：登录")
@pytest.fixture
def test_loginss(request):
    params = request.param
    name = params["username"]
    pwd = params["pwd"]
    allure.attach(f"这是测试用例传的参数{params}")
    print(name,pwd,params)
    yield name,pwd


@allure.title("成功登录，测试数据是：{test_loginss}")
@pytest.mark.parametrize("test_loginss", [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"}], indirect=True)
def test_success_login(test_loginss):
    name, pwd = test_loginss
    allure.attach(f"账号{name},密码{pwd}")


@allure.title("多个参数{name},{phone},{age}")
@pytest.mark.parametrize("name,phone,age", [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
def test_test_test(name, phone, age):
    print(name, phone, age)