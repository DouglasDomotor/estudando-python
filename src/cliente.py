from calculadora_idade import *

class Cliente:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        
    def fale_seu_nome(self):
        return f"Meu nome é {self.nome}"
    
    def idade(self):
        return CalculadoraIdade.calcular_idade(self.data_nascimento)
