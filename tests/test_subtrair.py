from subtrair import subtrair
import pytest

def test_subtrair():
    assert subtrair(1, 1) == 0
    assert subtrair(3, 1) == 2
