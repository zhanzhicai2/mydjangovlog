import pytest



def f():
    return 6
def f2():
    return "hello"

def test_function_assert():
    a = f()
    assert a % 2 == 0,"判断a为偶数，当前a的值为%s" % a


def test_function_f2assert():
    a = f2()
    assert a == "hello"
    #判断相等
    # assert not a
    #判断是假
    assert "h" in a
    #判断包含
    assert "hell" != a
    # 判断不相等
#断言异常
def test_function_raises():
    with pytest.raises(ZeroDivisionError):
        1/0
        # 断言异常类型 type
        assert excinfo.type == ZeroDivisionError
        #断言异常 value
        assert "division by zero" in str(excinfo.value)

# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_function_rasises_Decorator():
    1 / 0