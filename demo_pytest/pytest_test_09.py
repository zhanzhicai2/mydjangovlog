import pytest

def test_1():
    assert 4+3 ==7

def test_2():
    assert 4+2 == 6

def test_3():
    assert 6*9 == 54

data_1 = [("3+5", 8), ("2+4", 6), ("6*9", 54)]
@pytest.mark.parametrize("test_input,expected", data_1)
def test_eval(test_input,expected):
    print(f"测试数据{test_input},期望结果{expected}")
    assert eval(test_input) == expected


data_2 = [(1,2,3),(4,5,9)]
@pytest.mark.parametrize('a,b,expect',data_2)
class TestParametrisz:
    def test_parametrize_1(self,a,b,expect):
        print(f"\n 测试函数11111， 测试数据为\n{a}-{b}")
        assert a+b == expect

    def test_parametrize_2(self,a,b,expect):
        print(f"\n 测试函数2222，测试数据{a}-{b}")
        assert a+b == expect


## 笛卡尔积，组合数据
data_3 = [1,2,3]
data_4 = ['a','b']
@pytest.mark.parametrize('a',data_3)
@pytest.mark.parametrize('b',data_4)
def test_parametrize(a,b):
    print(f"笛卡尔积，测试数据为：{a}-{b}")

# 字典
data_5 = (
    {
        'user': 1,
        'pwd': 2
    },
    {
        "user": 3,
        "pwd": 4
    }
)

@pytest.mark.parametrize('dic',data_5)
def test_parametrize_5(dic):
    print(f"测试数据为：{dic}")
    # print({dic['user']},{dic["pwd"]})
    print(f"user:{dic['user']},pwd:{dic['pwd']}")
    # print(f"user:{dic['user']},pwd:{dic['pwd']}")

# 参数化，标记数据


@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),
    ("8+9",17)
    # pytest.param("6*9",42,marks = pytest.mark.xfail),
    # pytest.param("6*6",42,marks=pytest.mark.skip)
])
def test_mark(test_input,expected):
    assert eval(test_input) == expected

# 参数化，增加可读性 ids

data_6 = [
    (1,2,3),
    (4,5,9)
]
#ids
ids = ["a:{}+b{} = expect:{}".format(a,b,expect) for a,b,expect in data_6]
@pytest.mark.parametrize('a,b,expect',data_6,ids=ids)
class TestParametrize_2(object):
    def test_parametrize_2_1(self,a,b,expect):
        print('测试函数1测试数据为{}-{}'.format(a,b))
        assert a+b ==expect
    def test_parametrize_2_2(self,a,b,expect):
        print('测试函数2测试数据为{}-{}'.format(a, b))
        assert a + b == expect