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
    
    def localizar_por_codigo(self, codigo):
        for acao in self.acoes:
            if acao.codigo == codigo:
                return acao
            
    def processar_venda(self, ordem):
        acao = self.localizar_por_codigo(ordem.codigo)
        if not acao:
            print("Erro: Ação não encontrada na carteira para venda.")
            return
        if ordem.quantidade > acao.quantidade:
            print(f"Erro: Você só possui {acao.quantidade} ações de {acao.codigo}.")
            return
        acao.quantidade -= ordem.quantidade
        if acao.quantidade == 0:
            self.acoes.remove(acao)

            
    def localizar_ou_criar_acao(self, ordem):
        acao = self.localizar_por_codigo(ordem.codigo)
        if acao:
            return acao
        else:
            acao = Acao(ordem.codigo, ordem.codigo, " ", ordem.valor, 0)
            self.adicionar_acao(acao)
            return acao
  
    def executar_ordem(self, ordem):
        if ordem.tipo == 'compra':
            acao = self.localizar_ou_criar_acao(ordem)
            acao.quantidade += ordem.quantidade
        elif ordem.tipo == 'venda':
            self.processar_venda(ordem)
        else:
            print("Tipo de ordem inválido. Use 'compra' ou 'venda'.")                 
