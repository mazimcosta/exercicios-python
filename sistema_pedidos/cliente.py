# Criando cliente



class   Cliente:

    def __init__(self,nome,email):
        if not isinstance(nome,str):
            raise ValueError('Nome invalido')
        elif not nome.strip().replace(' ','').isalpha():
            raise ValueError('Nome invalido')
        if not isinstance(email,str):
            raise ValueError('Email invalido')
        
        partes=email.split('@')
        if len(partes)!=2:
            raise ValueError('Email invalido')
        elif  not partes[0].strip().replace(' ',''):
            raise ValueError('Email invalido')
        elif partes[1].startswith('.'):
            raise ValueError('Email invalido')
        elif '.' not in partes[1]:
            raise ValueError('Email invalido')
        elif partes[1].endswith('.'):
            raise ValueError('Email invalido')
        self.nome=nome
        self.email=email