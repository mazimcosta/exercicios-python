#Construindo a classe carrinho
from servicos import desconto_geral
from produto import Produto
class Carrinho:

    def __init__(self,cliente:str,itens:list):
        self.cliente=cliente
        self.itens=list(itens)

    def adicionar_produto(self,produto):
        if produto.estoque>0:
            self.itens.append(produto)
            produto.estoque-=1
            return f' produto adicionado com sucesso.'
        return f'Produto indisponivel.'
    
    def remover_produto(self,codigo):
        for produto in self.itens:
            if produto.codigo==codigo:
                self.itens.remove(produto)
                return f' produto removido'
        return f'Produto inexistente.'
    
    def exibir_produtos(self):
        for produto in self.itens:
            return f'produto: {produto.nome}'
        if not self.itens:
            return f' carrinho vazio'


    def exibir_quantidade(self):
        return f'produtos no carrinho :{len(self.itens)}'


    def total_compras(self):
        total=0
        if not self.itens:
            return f'carrinho vazio.'
        else:
            for produto in self.itens:
                total+=produto.preco
            return total

    def desconto_itens(itens,percentual):
      return  desconto_geral(itens,percentual)

    def finalizar_compras(self):
        return f' total :{self.total_compras()}'

