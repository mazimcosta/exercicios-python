#Criando a classe produtos


class Produto:

    def __init__(self,nome:str,preco:float,estoque:int):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

    def baixar_estoque(self,quantidade):
        if self.estoque==0:
            raise ValueError(' Não ha produtos no estoque')
        if quantidade>self.estoque:
            raise ValueError('Estoque insuficiente')
        self.estoque-=quantidade
        return f' Quantidade retirada com sucesso'
    
    def devolver_estoque(self,quantidade):
        if quantidade<=0:
            raise ValueError('Valor invalido')
        self.estoque+=quantidade
        return f' Estoque reposto com sucesso'
    
    