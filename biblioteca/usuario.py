#Criando a classe usuarios:

class Usuario:


    def __init__(self,nome,id_usuario):
        if not isinstance(nome,str):
            raise ValueError("Nome invalido")
        
        nome=nome.strip()

        if not nome.replace(' ','').isalpha():
            raise ValueError('Nome invalido')
        
        if not isinstance(id_usuario,str):
            raise ValueError('Id invalida')
        
        id_usuario=id_usuario.strip()

        if not id_usuario.replace(' ',''):
            raise ValueError('Id invalida')
        
        self.nome=nome
        self.id_usuario=id_usuario
        self.__lista_emprestimos=[]


    @property
    def lista_emprestimos(self):
        return self.__lista_emprestimos.copy()
    

    def pegar_livro(self,livro):
        if not livro.disponivel:
            raise ValueError('Livro indisponivel')
        
        if len(self.__lista_emprestimos)>=3:
            raise ValueError('Usuario atingiu limite de emprestimos')

        livro.emprestar()
        self.__lista_emprestimos.append(livro)

        return f'Emprestimo feito com sucesso'

    def devolver_livro(self,livro):
        if livro.disponivel:
            raise ValueError('O livro esta disponivel')
        
        if livro not in self.__lista_emprestimos:
            raise ValueError('O livro nao se encontra emprestado')
        
        livro.devolver()
        self.__lista_emprestimos.remove(livro)

        return f'Devolução feita com sucesso'
    
    def __str__(self):
        return f'Usuario: nome={self.nome} id={self.id_usuario}'
    
    