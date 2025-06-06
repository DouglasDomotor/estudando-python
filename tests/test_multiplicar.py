from multiplicar import multiplicar
import pytest

@pytest.mark.parametrize("numero, mult_numero, resultado", [
    (1, 2, 2),
    (3, 2, 6),
])

def test_multiplicar(numero, mult_numero, resultado):
    assert multiplicar(numero, mult_numero) == resultado
