from utils.calculadora_idade import CalculadoraIdade

class Cliente:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.acoes = []
        
    def fale_seu_nome(self):
        return f"Meu nome é {self.nome}"
    
    def idade(self):
        return CalculadoraIdade.calcular_idade(self.data_nascimento)
    
    def adicionar_acao(self, acao):
        self.acoes.append(acao)

    def saldo(self):
        saldo = 0
        for acao in self.acoes:
            saldo += acao.saldo()
        return saldo
