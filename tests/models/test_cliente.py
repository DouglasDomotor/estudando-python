from models.cliente import Cliente
from models.acao import Acao
from models.ordem import Ordem
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

def test_executar_ordem_compra():
    cliente = Cliente("Douglas", "05/11/1982")
    ordem_compra = Ordem('compra', 'VALE3', 1, 45.00)
    cliente.executar_ordem(ordem_compra) 
    acao = cliente.acoes[0]  

    assert acao.codigo == "VALE3"
    assert acao.quantidade == 1
    assert acao.saldo() == 45.00

    ordem_compra = Ordem('compra', 'VALE3', 1, 45.00)
    cliente.executar_ordem(ordem_compra) 
    acao = cliente.acoes[0]  

    assert acao.quantidade == 2
    assert acao.saldo() == 90.00  
    assert len(cliente.acoes) == 1
    assert cliente.acoes[0].quantidade == 2

def test_executar_ordem_dupla_compra():
    cliente = Cliente("Douglas", "05/11/1982")
    ordem_compra_vale = Ordem('compra', 'VALE3', 100, 45.00)
    ordem_compra_petro = Ordem('compra', 'PETR4', 200, 30.00)
    cliente.executar_ordem(ordem_compra_vale)
    cliente.executar_ordem(ordem_compra_petro)
    acao_vale = cliente.localizar_por_codigo('VALE3')

    assert acao_vale.codigo == 'VALE3'
    assert acao_vale.quantidade == 100
    assert acao_vale.saldo() == 4500

    acao_petro = cliente.localizar_por_codigo('PETR4')

    assert acao_petro.codigo == 'PETR4'
    assert acao_petro.quantidade == 200
    assert acao_petro.saldo() == 6000

    assert len(cliente.acoes) == 2
    assert cliente.saldo() == 10500

def ordem_de_venda_inexistente():
    cliente = Cliente("Douglas", "05/11/1982")
    ordem_compra = Ordem('compra', 'VALE3', 100, 45.00)
    cliente.executar_ordem(ordem_compra) 

    ordem_venda_inexistente = Ordem('venda', 'PETR3', 100, 30.00)
    cliente.executar_ordem(ordem_venda_inexistente)

    codigos = [a.codigo for a in cliente.acoes]
    assert 'PETR3' not in codigos   

def test_executar_ordem_venda_sem_ter_acoes():
    cliente = Cliente("Douglas", "05/11/1982")
    
    ordem_venda = Ordem('venda', 'VALE3', 1, 45.00)
    cliente.executar_ordem(ordem_venda)
    
    assert len(cliente.acoes) == 0
  

# def test_executar_ordem():
#     cliente = Cliente("Douglas", "05/11/1982")

#     ordem_compra1 = Ordem('compra', 'VALE3', 100, 45.00)
#     cliente.executar_ordem(ordem_compra1)

#     acao = cliente.acoes[0]

#     assert acao.codigo == "VALE3"
#     assert acao.quantidade == 100
#     assert acao.saldo() == 4500

#     ordem_compra2 = Ordem('compra', 'VALE3', 10, 45.00)
#     cliente.executar_ordem(ordem_compra2)

#     assert acao.quantidade == 110
#     assert acao.saldo() == 4950

#     ordem_venda1 = Ordem('venda', 'VALE3', 10, 50.00)
#     cliente.executar_ordem(ordem_venda1)

#     assert acao.quantidade == 100
#     assert acao.saldo() == 4500

#     ordem_venda_inexistente = Ordem('venda', 'PETR3', 100, 30.00)
#     cliente.executar_ordem(ordem_venda_inexistente)

#     codigos = [a.codigo for a in cliente.acoes]
#     assert 'PETR3' not in codigos   
