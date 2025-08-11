class Ordem:
    def __init__(self, tipo, codigo, quantidade, valor):
        self.tipo = tipo
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor = valor
        
    def total(self):
        return self.quantidade * self.valor
