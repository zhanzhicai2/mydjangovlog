import demo
from unittest import mock

def need_mock_fun():
    # mock_get_sum = mock.patch('demo.get_sum',new=20, side_effect=demo.mock_fun)
    mock_get_sum = mock.patch('demo.get_sum', new=20)
    mock_get_sum.start()
    result = demo.get_sum
    mock_get_sum.stop()
    print(result)


need_mock_fun()