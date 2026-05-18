#Começando a classe pedido:
from produto import Produto
from cliente import Cliente


class  Pedido:

    def __init__(self,cliente,status='criado'):
        if not isinstance(cliente,Cliente):
            raise ValueError('Cliente invalido')
        self.cliente=cliente
        self.status=status
        self.itens=list()



    def adicionar_produto(self,produto,quantidade):
        if self.status!='criado':
            raise ValueError('Nao e possivel adicionar mais produtos')
       
        if not isinstance(produto,Produto):
            raise ValueError('Produto invalido')
        elif not isinstance(quantidade,int):
            raise ValueError('Quantidade invaida')
        elif quantidade<=0:
            raise ValueError('Quantidade invalida')
        elif quantidade>produto.estoque:
            raise ValueError('Estoque insuficiente')
        
        

        self.itens.append({
            'produto':produto,
            'nome':produto.nome,
            'preco':produto.preco,
            'quantidade':quantidade,
            'subtotal':round((produto.preco * quantidade),2)
        })


    def remover_produto(self,nome_produto):
        if self.status!='criado':
            raise ValueError('Nao e possivel remover os produtos')
        for item in self.itens:
            if nome_produto==item['nome']:
                
                self.itens.remove(item)
                return f'Produto removido com sucesso'
        raise ValueError('Produto nao encontrado')
        
    def calcular_total(self):
        total=0
        for item in self.itens:
            total+=item['subtotal']
        return round(total,2)
    
    def finalizar_pedido(self):
        if self.status!='criado':
            raise ValueError('Nao e possivel finalizar pedido')
        if not self.itens:
            raise ValueError('Nao ha itens no pedido')
        self.status='pago'
        for item in self.itens:
            item['produto'].baixar_estoque(item['quantidade'])
        return f'Pedido finalizado com sucesso'

    def enviar_pedido(self):
        if self.status=='enviado':
            raise ValueError('Pedido ja enviado')
        if self.status!='pago':
            raise ValueError('Pagamento nao efetuado')
        self.status='enviado'
        return f'Pedido enviado com sucesso'
    
    def  cancelar_pedido(self):
        if self.status=='enviado':
            raise ValueError('Pedido nao pode ser cancelado')
        
        if self.status=='criado':
            self.status='cancelado'
            return f'Pedido cancelado com sucesso'
        
        
        if  self.status=='pago':
            for item in self.itens:
                item['produto'].devolver_estoque(item['quantidade'])
            self.status='cancelado'
            return f'Pedido cancelado com sucesso'
        raise ValueError('Pedido ja foi cancelado')
    
    def __str__(self):
        cliente=self.cliente.nome
        produtos=len(self.itens)
        valor=self.calcular_total()
        status=self.status

        return f'Cliente:{cliente} produtos{produtos} valor:{valor} status:{status}'
    
        

