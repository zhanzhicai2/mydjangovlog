import pytest


@pytest.mark.flaky(reruns = 5)
def test_example():
    # import random
    assert 1+2 == 2

