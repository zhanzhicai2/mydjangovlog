import pytest

@pytest.fixture(scope="session")
def open_51(login):
    name,token = login
    print(f"###用户{name},打开51job网站###")
