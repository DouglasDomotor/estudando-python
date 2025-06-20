from models.cliente import Cliente
from models.acao import Acao
from freezegun import freeze_time
import pytest

@freeze_time("2025-06-06")
def test_cliente_inicializacao():
    cliente = Cliente("Douglas", "05/11/1982")
    assert cliente.nome == "Douglas"
    assert cliente.data_nascimento == "05/11/1982"
    assert cliente.fale_seu_nome() == "Meu nome é Douglas"
    assert cliente.idade() == 42

def test_adicionar_acao():
    cliente = Cliente("Douglas", "05/11/1982")
    vale = Acao("VALE", "VALE3", "Mineração", 50.00, 100)
    cliente.adicionar_acao(vale)
    assert cliente.acoes[0].codigo == 'VALE3'

    petr = Acao("PETR", "PETR4", "Petróleo", 30.00, 200)
    cliente.adicionar_acao(petr)
    assert cliente.acoes[1].codigo == 'PETR4'

def test_saldo():
    cliente = Cliente("Douglas", "05/11/1982")
    vale = Acao("VALE", "VALE3", "Mineração", 50.00, 100)
    cliente.adicionar_acao(vale)
    petr = Acao("PETR", "PETR4", "Petróleo", 30.00, 200)
    cliente.adicionar_acao(petr)
    assert cliente.saldo() == 11000
