
# =============================================================================
# EXERCÍCIO 21 | Sistema de Biblioteca (Boss Fight)
# Nível: Muito Difícil
# Contexto: Modelagem orientada a objetos + regras de negócio
# =============================================================================

"""
CONTEXTO:
Você vai construir um mini sistema de biblioteca orientado a objetos.

Esse exercício testa:
- POO
- encapsulamento
- listas
- validações
- responsabilidade entre classes
- regras de negócio
- modelagem
- exceptions
- pensamento backend

OBJETIVO:
Criar um sistema funcional de empréstimo de livros.
"""

# -------------------------------------------------------------------------
# CLASSES OBRIGATÓRIAS
# -------------------------------------------------------------------------

"""
1) Classe Livro
Responsabilidade:
Representar um livro da biblioteca.

Atributos:
- titulo
- autor
- isbn
- disponivel (bool)

Regras:
- título e autor não podem ser vazios
- isbn não pode ser vazio

Métodos:
- emprestar()
    -> marca como indisponível
    -> se já estiver emprestado, lançar erro

- devolver()
    -> marca como disponível
    -> se já estiver disponível, lançar erro

- __str__()
"""


"""
2) Classe Usuario
Responsabilidade:
Representar usuário da biblioteca.

Atributos:
- nome
- id_usuario
- livros_emprestados (lista)

Regras:
- nome obrigatório
- id obrigatório

Métodos:
- pegar_livro(livro)
- devolver_livro(livro)
- __str__()
"""


"""
3) Classe Biblioteca
Responsabilidade:
Gerenciar sistema inteiro.

Atributos:
- nome
- livros (lista)
- usuarios (lista)

Métodos:
- adicionar_livro(livro)
- cadastrar_usuario(usuario)

- buscar_livro_por_isbn(isbn)
    -> retorna livro ou None

- buscar_usuario_por_id(id_usuario)
    -> retorna usuario ou None

- emprestar_livro(id_usuario, isbn)

Fluxo:
1. localizar usuário
2. localizar livro
3. validar existência
4. validar disponibilidade
5. validar limite do usuário
6. emprestar

- devolver_livro(id_usuario, isbn)

Fluxo:
1. localizar usuário
2. localizar livro
3. validar
4. devolver

- listar_livros_disponiveis()

- listar_livros_emprestados()

- __len__()
    -> quantidade de livros cadastrados
"""


# -------------------------------------------------------------------------
# REGRAS DE NEGÓCIO
# -------------------------------------------------------------------------

"""
REGRAS:

1. Usuário pode ter no máximo 3 livros emprestados.

2. Não pode emprestar livro indisponível.

3. Não pode devolver livro que não está emprestado.

4. Não pode cadastrar ISBN duplicado.

5. Não pode cadastrar usuário duplicado.

6. Buscar deve retornar None quando não encontrar.

7. Use raise ValueError para regras quebradas.
"""


# -------------------------------------------------------------------------
# TESTES OBRIGATÓRIOS
# -------------------------------------------------------------------------

"""
TESTE CENÁRIOS:

[ ] cadastrar livros
[ ] cadastrar usuários
[ ] emprestar livro
[ ] tentar emprestar indisponível
[ ] devolver livro
[ ] tentar devolver livro inválido
[ ] exceder limite usuário
[ ] buscar livro
[ ] buscar usuário
[ ] listar disponíveis
[ ] listar emprestados
[ ] usar len(biblioteca)
"""


# -------------------------------------------------------------------------
# DESAFIOS EXTRAS (OPCIONAL)
# -------------------------------------------------------------------------

"""
SE SOBRAR ENERGIA:

1. histórico de empréstimos
2. top livros mais emprestados
3. busca por título
4. remover livro
5. remover usuário
"""