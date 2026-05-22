#Construindo a classe livro:


class Livro:


    def  __init__(self,titulo,autor,isbn):

        if not isinstance(titulo,str):
            raise ValueError('Titulo invalido')
        
        titulo=titulo.strip()

        if not titulo.replace(' ',''):
            raise ValueError('Titulo invalido')
        
        if not isinstance(autor,str):
            raise ValueError('Autor invalido')
        
        autor=autor.strip()


        if not autor.replace(' ',''):
            raise ValueError('Autor invalido')
        

        if not isinstance(isbn,str):
            raise ValueError('ISBN invalido')
        
        isbn=isbn.strip()

        if not isbn.replace(' ',''):
            raise ValueError('ISBN invalido')
        
        
        
        
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.__disponivel=True


    @property
    def disponivel(self):
        return self.__disponivel
    

    def emprestar(self):
        if not self.disponivel:
            raise ValueError('Livro indisponivel')
        
        self.__disponivel=False
        return f'Emprestimo realizado com sucesso'
    
    def devolver(self):
        if self.disponivel:
            raise ValueError('Livro ja disponivel')
        
        self.__disponivel=True
        return 'Devolução feita com sucesso'
    
    def __str__(self):
        return f'Livro: titulo={self.titulo} autor={self.autor} ISBN={self.isbn}'
    
    