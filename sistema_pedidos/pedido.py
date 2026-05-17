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
            raise ValueError('Nao e possivel fazer outro pedido')
        if produto not in itens:
            raise ValueError( f'Produto nao encontrado')
        if not isinstance(quantidade,int):
            raise ValueError('Valor invalido')
        
        if quantidade<=0:
            raise ValueError('Quantidade invalida')
        if quantidade>produto.estoque:
            raise ValueError('Quantidade indisponivel')

        self.produtos.append({
            produto:{'nome':produto.nome,
                'preco':produto.preco,
                'quantidade':quantidade,
                'subtotal':round(float(produto.preco * quantidade),2)
            }
        })

    def remover_produto(self,nome_produto):
        for produto in self.produtos:
            if nome_produto==produto['nome']:
                quantidade=produto['quantidade']
                produto.devolver_estoque(quantidade)
                self.produtos.remove(produto)
                return f'Produto removido com sucesso'
            else:
                raise ValueError('Produto não encontrado')
        return
    
    def calcular_total(self):
        valor=0
        for produto in self.produtos:
            valor+=produto['preco']
        return f'total:{valor:.2f}'
