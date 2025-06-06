from subtrair import subtrair
import pytest

@pytest.mark.parametrize("numero_1, numero_2, resultado",[
    (5, 2, 3),
    (10, 3, 7)
])

def test_subtrair(numero_1, numero_2, resultado):
    assert subtrair(numero_1, numero_2) == resultado
