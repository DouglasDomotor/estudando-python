class Calculadora:
    def __init__(self):
        pass

    @staticmethod
    def soma(a, b):
        return  a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Divisão por zero não é permitida."
        return a / b
        
