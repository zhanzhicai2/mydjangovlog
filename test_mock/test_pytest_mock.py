from unittest import mock
import demo
import pytest

def test_mock_fun(mocker):
    mock_get_sum = mocker.patch('demo.get_sum')
    mock_get_sum.return_value = 20
    print(mock_get_sum())

def foo(param):
    param('foo','bar')

def test_stub(mocker):
    #构造模拟函数
    stub = mocker.stub(name='on_something_stub')
    foo(stub)
    # 测试foo函数调用是否正确
    stub.assert_called_once_with('foo', 'bar')

def test_pytest_mock_fun():
    mock_get_sum = mock.patch('demo.get_sum', return_value = 20)
    print(demo.get_sum(1,2))


test_pytest_mock_fun()