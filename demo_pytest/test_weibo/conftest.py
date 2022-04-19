import pytest


@pytest.fixture(scope="function")
def open_weibo(login):
    name,token = login
    print(f"&&&用户名{name}返回微博首页&&&")
