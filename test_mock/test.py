from unittest import mock
def gets_sum(x,y):
    pass
def mock_fun():
    return 40
# mock_fun()
def wrap_fun():
    return mock_fun()


# if __name__ == '__main__':
#     a = 100
#     b = 200
#     # gets_sum = mock.Mock(return_value=20, side_effect=mock_fun)
#     gets_sum= mock.Mock(wraps=wrap_fun)
#     result = gets_sum()
#     print(result)
def need_mock_fun():
    a = 100
    b = 200
    gets_sum = mock.Mock(return_value = 20,side_effect = mock_fun)
    result = gets_sum()
    print(result)

need_mock_fun()