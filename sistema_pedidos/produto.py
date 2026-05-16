#Criando a classe produtos


class Produto:

    def __init__(self,nome:str,preco:float,estoque:int):
        if not isinstance(preco,float):
            raise ValueError('Preco invalido')
        elif preco<0:
            raise ValueError('Preco invalido')
        elif not isinstance(nome,str):
            raise ValueError('Nome precisa ser um texto')
        elif  not nome.replace(' ','').isalpha():
            raise ValueError('Nome deve conter apenas letras')
        elif estoque<0:
            raise ValueError('Estoque não pode ser negativo')
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

    def baixar_estoque(self,valor):
        if valor<0:
            raise ValueError('Valor invalido')
        elif valor>self.estoque:
            raise ValueError('Estoque insuficiente')
        self.estoque-=valor
        return f'Estoque reduzido com sucesso'
    
    def devolver_estoque(self,valor):
        if valor<0:
            raise ValueError('Valor invalido')
        self.estoque+=valor
        return f'Estoque reposto com sucesso'