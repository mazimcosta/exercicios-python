#Criando a classe produto


class    Produto:


    def __init__(self,nome,preco,estoque):
        if not isinstance(nome,str):
            raise ValueError('Nome invalido')
        elif not nome.strip().replace(' ','').isalpha():
            raise ValueError('Nome invalido')
        elif not isinstance(preco,(int,float)):
            raise ValueError('Preco invalido')
        elif preco<=0:
            raise ValueError('Preco invalido')
        elif not isinstance(estoque,int):
            raise ValueError('Estoque invalido')
        elif estoque<0:
            raise ValueError('Estoque invalido')
        
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

    def   baixar_estoque(self,quantidade):
        if not isinstance(quantidade,int):
            raise ValueError('Quantidade invalida')
        elif quantidade<=0:
            raise ValueError('Quantidade invalida')
        elif quantidade>self.estoque:
            raise ValueError(' Estoque insuficiente')
        self.estoque-=quantidade
        return 
    

    
    def  devolver_estoque(self,quantidade):
        if not isinstance(quantidade,int):
            raise ValueError('Quantidade invalida')
        elif quantidade<=0:
            raise ValueError('Quantidade invalida')
        self.estoque+=quantidade
        return