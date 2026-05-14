# "PARTE 1 — Classe Produto

# "Crie a classe Produto com:
# - __init__(self, codigo, nome, preco, estoque)
# - aplicar_desconto(percentual: float) → altera o preço
# - adicionar_estoque(qtd: int)
# - remover_estoque(qtd: int) → raise ValueError se insuficiente
# - esta_disponivel() -> bool
# - valor_em_estoque() -> float (preco * estoque)
# - __str__() → representação legível
# - __repr__() → representação técnica

# REGRAS:
# - preco e estoque não podem ser negativos
#- usar @property para preco (com validação).


class Produto:

    def __init__(self,codigo,nome,preco,estoque):
        self.codigo=codigo
        self.nome=nome
        self._preco=preco
        self.estoque=estoque

    def aplicar_desconto(self,percentual:float):
        if percentual>100:
            raise ValueError(' O percentual não pode ser superior a 100%')
        self._preco=round((self._preco * percentual)/100,2)

    def adicionar_estoque(self,qtd:int):
        if qtd<0:
            raise ValueError('O estoque não pode ser negativo')
        self.estoque+=qtd

    def remover_estoque(self,qtd:int):
        if qtd<0:
            raise ValueError('O estoque não pode ser negativo')
        self.estoque-=qtd

    def esta_disponivel(self):
        if self.estoque>0:
            return True
        return False
    
    def valor_em_estoque(self):
        return round(self._preco * self.estoque,2)
    

    def __str__(self):
        return f'codigo={self.codigo} nome={self.nome} preco={self.preco:.2f} estoque={self.estoque}'
    
    def __repr__(self):
        return f'Produto(codigo={self.codigo}, nome={self.nome}, preco={self.preco:.2f}, estoque={self.estoque})'
    
    