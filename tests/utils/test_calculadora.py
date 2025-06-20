from utils.calculadora import *
import pytest

def test_soma():
    assert Calculadora.soma(1, 1) == 2
    assert Calculadora.soma(1, 2) == 3
    assert Calculadora.soma(-1, 2) == 1
    assert Calculadora.soma(2, -1) == 1
    assert Calculadora.soma(-1, -2) == -3

def test_subitrair():
    assert Calculadora.subtrair(2, 1) == 1
    assert Calculadora.subtrair(5, 1) == 4
    assert Calculadora.subtrair(5, 3) == 2
    assert Calculadora.subtrair(-5, -1) == -4
    assert Calculadora.subtrair(2, 1) == 1

def test_multiplicar():
    assert Calculadora.multiplicar(1, 1) == 1
    assert Calculadora.multiplicar(1, 2) == 2
    assert Calculadora.multiplicar(4, 1) == 4
    assert Calculadora.multiplicar(4, 3) == 12
    assert Calculadora.multiplicar(-1, 1) == -1
    assert Calculadora.multiplicar(-2, -2) == 4

def test_dividir():
    assert Calculadora.dividir(1, 1) == 1
    assert Calculadora.dividir(2, 1) == 2
    assert Calculadora.dividir(1, 2) == 0.5
    assert Calculadora.dividir(7, 2) == 3.5
    assert Calculadora.dividir(1, 0) == "Divisão por zero não é permitida."
