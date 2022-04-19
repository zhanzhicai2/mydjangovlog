from unittest import mock
import test_demo_2


@mock.patch('test_demo_2.get_sum')
def need_mock_fun(mock_get_sum):
    mock_get_sum.return_value = 20
    result = test_demo_2.get_sum()
    print('need_mock_fun:{}'.format(result))


need_mock_fun()


def mock_fun():
    return 30


@mock.patch("test_demo_2.get_sum")
def need_mock_fun_1(mock_get_sum):
    mock_get_sum.return_value = 20
    mock_get_sum.side_effect = mock_fun
    result = test_demo_2.get_sum()
    print('need_mock_fun_1:{}'.format(result))


need_mock_fun_1()

