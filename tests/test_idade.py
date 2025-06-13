import pytest
from freezegun import freeze_time
from idade import calcular_idade

@freeze_time("2025-06-06")
@pytest.mark.parametrize("nascimento, idade_esperada", [
    ("01/06/2000", 25),
    ("06/06/2000", 25),
    ("10/06/2000", 24),
]) 
def test_vcalculo_idade(nascimento, idade_esperada):
    assert calcular_idade(nascimento) == idade_esperada
    
