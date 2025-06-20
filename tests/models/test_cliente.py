from models.cliente import Cliente
from freezegun import freeze_time
import pytest

@freeze_time("2025-06-06")
def test_cliente_inicializacao():
    cliente = Cliente("Douglas", "05/11/1982")
    assert cliente.nome == "Douglas"
    assert cliente.data_nascimento == "05/11/1982"
    assert cliente.fale_seu_nome() == "Meu nome é Douglas"
    assert cliente.idade() == 42
