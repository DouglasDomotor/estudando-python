from calculadora_idade import CalculadoraIdade
from freezegun import freeze_time
import pytest

@freeze_time("2025-06-06")
def test_calculo_idade_em_bloco():
    assert CalculadoraIdade.calcular_idade("01/06/2000") == 25
    assert CalculadoraIdade.calcular_idade("06/06/2000") == 25
    assert CalculadoraIdade.calcular_idade("10/06/2000") == 24
    assert CalculadoraIdade.calcular_idade("06/06/2025") == 0 

@freeze_time("2025-06-06")
def test_data_futura_gera_erro():
    with pytest.raises(ValueError):
        CalculadoraIdade.calcular_idade("07/06/2025")
