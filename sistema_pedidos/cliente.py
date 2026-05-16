#Criando a classe clientes

class Cliente:

    def __init__(self,nome:str,email:str):
        if not nome.replace(' ','').isalpha():
            raise ValueError(' Nome precisa ser um texto')
        elif '@' not in email and '.' not in email.split('@')[1]:
            raise ValueError('Email invalido')
        elif not (email.endswith('.com') or  email.endswith('.br')):
            raise ValueError('Email invalido')
        self.nome=nome
        self.email=email