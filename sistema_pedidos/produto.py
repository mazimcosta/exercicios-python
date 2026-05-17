#Criando a classe produtos


class Produto:

    def __init__(self,nome:str,preco:float,estoque:int):
        if not isinstance(preco,(float,int)):
            raise ValueError('Preco invalido')
        elif preco<=0:
            raise ValueError('Preco invalido')
        elif not isinstance(nome,str):
            raise ValueError('Nome precisa ser um texto')
        elif  not nome.replace(' ','').isalpha():
            raise ValueError('Nome deve conter apenas letras')
        elif not isinstance(estoque,int):
            raise ValueError('Valor invalido')
        
        elif estoque<=0:
            raise ValueError('Estoque não pode ser negativo')
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

    def baixar_estoque(self,valor):
        if valor<=0:
            raise ValueError('Valor invalido')
        elif valor>self.estoque:
            raise ValueError('Estoque insuficiente')
        self.estoque-=valor
        return 
    
    def devolver_estoque(self,valor):
        if valor<=0:
            raise ValueError('Valor invalido')
        self.estoque+=valor
        return 