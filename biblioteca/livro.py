#Construindo a classe livro:


class Livro:


    def  __init__(self,titulo,autor,isbn,disponivel):

        if not isinstance(titulo,str):
            raise ValueError('Titulo invalido')
        
        titulo=titulo.strip()

        if not titulo.replace(' ',''):
            raise ValueError('Titulo invalido')
        
        if not isinstance(autor,str):
            raise ValueError('Autor invalido')
        
        autor=autor.strip()


        if not autor.replace(' ','').isalpha():
            raise ValueError('Autor invalido')
        

        if not isinstance(isbn,str):
            raise ValueError('ISBN invalido')
        
        isbn=isbn.strip()

        if not isbn.replace(' ',''):
            raise ValueError('ISBN invalido')
        
        if disponivel not in [True,False]:
            raise ValueError('Disponibilidade invalida')
        
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.disponivel=disponivel