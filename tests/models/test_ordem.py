from models.ordem import Ordem
import pytest

def test_ordem():
    ordem = Ordem('compra', 'VALE3', 100, 45.00)
    assert ordem.tipo == 'compra'
    assert ordem.codigo == 'VALE3'
    assert ordem.quantidade == 100
    assert ordem.valor == 45.00
