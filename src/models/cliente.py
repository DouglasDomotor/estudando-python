from utils.calculadora_idade import CalculadoraIdade
from models.acao import Acao

class Cliente:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.acoes = []
        self.ordens = []
        
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
    
    def executar_ordem(self, ordem):
        if ordem.tipo == 'compra':
            for acao in self.acoes:
                 if acao.codigo == ordem.codigo:
                    acao.quantidade += ordem.quantidade
                    break
            else:
                nova_acao = Acao(ordem.codigo, ordem.codigo, " ", ordem.valor, ordem.quantidade)
                self.acoes.append(nova_acao)

        elif ordem.tipo == "venda":
            for acao in self.acoes:
                if acao.codigo == ordem.codigo:
                    if acao.quantidade >= ordem.quantidade:
                        acao.quantidade -= ordem.quantidade
                        if acao.quantidade == 0:
                            self.acoes.remove(acao)
                    else:
                        print(f"Erro: Você só possui {acao.quantidade} ações.")
                    break
            else:
                print("Erro: Ação não encontrada na carteira para venda.")

        else:
            print("Tipo de ordem inválido. Use 'compra' ou 'venda'.")

        self.ordens.append(ordem)                        
