class Acao:
    def __init__(self, nome, codigo, setor, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.setor = setor
        self.preco = preco
        self.quantidade = quantidade   

    def saldo(self):
        return self.quantidade * self.preco
        