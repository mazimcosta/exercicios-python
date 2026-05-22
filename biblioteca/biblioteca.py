#Criando a classe biblioteca
from livro import Livro
from usuario import Usuario

class Biblioteca:

    def  __init__(self,nome):
        if not isinstance(nome,str):
            raise ValueError('Nome invalido')

        nome=nome.strip()
        
        if not nome.replace(' ',''):
            raise ValueError('Nome invalido')
        
        self.nome=nome
        self.__livros=[]
        self.__usuarios=[]

    @property
    def livros(self):
        return self.__livros.copy()
    
    @property
    def usuarios(self):
        return self.__usuarios.copy()
    
    def adicionar_livro(self, livro):
            if not isinstance(livro, Livro):
              raise ValueError("Livro invalido")

            livro_existente = self.buscar_livro_isbn(livro.isbn)

            if livro_existente is not None:
              raise ValueError("Livro ja cadastrado")

            self.__livros.append(livro)
            return "Livro cadastrado com sucesso"

    
    def cadastrar_usuario(self, usuario):
            if not isinstance(usuario, Usuario):
                raise ValueError("Usuario invalido")

            usuario_existente = self.buscar_usuario_id(usuario.id_usuario)

            if usuario_existente is not None:
                raise ValueError("Usuario ja cadastrado")

            self.__usuarios.append(usuario)
            return "Usuario cadastrado com sucesso"





    def buscar_livro_isbn(self,isbn):
        if not isinstance(isbn, str):
            raise ValueError('ISBN invalido')
        
        isbn=isbn.strip()
        if not isbn.replace(' ',''):
            raise ValueError('ISBN invalido')
        
        for livro in self.__livros:
            if livro.isbn==isbn:
                return livro

        return None
    
    def buscar_usuario_id(self,id_usuario):
        if not isinstance(id_usuario,str):
            raise ValueError('ID invalida')
        
        id_usuario=id_usuario.strip()
        if not id_usuario.replace(' ',''):
            raise ValueError('ID invalido')
        
        for usuario in self.__usuarios:
            if usuario.id_usuario==id_usuario:
                return usuario

        return None
    
    def emprestar_livro(self, id_usuario, isbn):
        usuario = self.buscar_usuario_id(id_usuario)
        if usuario is None:
            raise ValueError("Usuario nao encontrado")

        livro = self.buscar_livro_isbn(isbn)
        if livro is None:
            raise ValueError("Livro nao encontrado")

        return usuario.pegar_livro(livro)





    

    def devolver_livro(self, id_usuario, isbn):
        usuario = self.buscar_usuario_id(id_usuario)
        if usuario is None:
            raise ValueError("Usuario nao encontrado")

        livro = self.buscar_livro_isbn(isbn)
        if livro is None:
            raise ValueError("Livro nao encontrado")

        return usuario.devolver_livro(livro)





    def livros_disponiveis(self):
        lista=[]
        for livro in self.__livros:
            if livro.disponivel:
                lista.append(livro)

        return lista    

    def livros_emprestados(self):
        lista=[]
        for usuario in self.__usuarios:
            for livro in usuario.lista_emprestimos:
                lista.append(livro)
        return lista
    
    
    def __len__(self):
        return len(self.__livros)    
