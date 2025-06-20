from models.acao import Acao
import pytest

def test_acao():
    vale = Acao("VALE", "VALE3", "Mineração", 50.00, 100)
    assert vale.nome == "VALE"
    assert vale.codigo == "VALE3"
    assert vale.setor == "Mineração"
    assert vale.preco == 50.00
    assert vale.quantidade == 100
    assert vale.saldo() == 5000.00
