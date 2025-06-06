from soma import soma
import pytest

@pytest.mark.parametrize("numero_1, numero_2, resultado",[
    (2, 2, 4),
])

def test_soma(numero_1, numero_2, resultado):
    assert soma(numero_1, numero_2) == resultado
