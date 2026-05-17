#Criando a classe clientes

class Cliente:

    def __init__(self,nome:str,email:str):
        if not isinstance(nome,str):
            raise ValueError('Nome precisa ser um texto')
        
        
        if not nome.replace(' ','').isalpha():
            raise ValueError(' Nome precisa ser um texto')
       
        if not isinstance(email,str):
            raise ValueError('Email invalido')
        if not '@' in email:
            raise ValueError('Email invalido')
        partes=email.split('@')
        if len(partes)!=2:
            raise ValueError('Email invalido')
        if  partes[1].endswith('.'):
            raise ValueError('Email invalido')
        self.nome=nome
        self.email=email