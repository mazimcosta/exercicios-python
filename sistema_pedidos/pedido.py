#Começando a classe pedido:
from produto import Produto
from cliente import Cliente
#Criando uma lista de produtos para o exercicio:
p1,p2,p3=Produto('arroz',4.99,75),Produto('feijao',7.99,50),Produto('macarrao',2.19,40)
itens=[p1,p2,p3]



class Pedido:

    def  __init__(self,cliente,produtos:list,status='criado'):
        self.cliente=cliente
        self.produtos=list(produtos)
        self.status=status


    def adicionar_produto(self,produto,quantidade):
        if self.status!='criado':
            return f' Nao e possivel fazer outro pedido'
        if produto not in itens:
            return f'Produto nao encontrado'
        if not isinstance(quantidade,int):
             return f'Digite um numero valido'
        
        if quantidade<=0:
            return f'Quantidade invalida'
        if quantidade>produto.estoque:
            return f'Quantidade indisponivel'
        
        produto.baixar_estoque(quantidade)

        self.produtos.append({
            produto.nome:{
                'preco':produto.preco,
                'quantidade':quantidade,
                'subtotal':round(float(produto.preco * quantidade),2)
            }
        })