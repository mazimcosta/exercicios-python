"""
# =============================================================================
# MINI PROJETO — Sistema de Produtos
# Nível: Iniciante / Intermediário
# =============================================================================

CONTEXTO:
Você irá simular um pequeno sistema de e-commerce utilizando Python.

OBJETIVO:
Praticar:
- Programação orientada a objetos (classes)
- Listas e dicionários
- Funções
- Lógica de programação
- Tratamento de erros

---------------------------------------------------------------------

PARTE 1 — Classe Produto

Crie a classe Produto com:
- __init__(self, codigo, nome, preco, estoque)
- aplicar_desconto(percentual: float) → altera o preço
- adicionar_estoque(qtd: int)
- remover_estoque(qtd: int) → raise ValueError se insuficiente
- esta_disponivel() -> bool
- valor_em_estoque() -> float (preco * estoque)
- __str__() → representação legível
- __repr__() → representação técnica

REGRAS:
- preco e estoque não podem ser negativos
- usar @property para preco (com validação)

---------------------------------------------------------------------

PARTE 2 — Cadastro de Produtos

Crie alguns produtos e armazene em uma lista:

Exemplo:
p1 = Produto(1, "Notebook", 3000, 5)
p2 = Produto(2, "Mouse", 100, 10)
p3 = Produto(3, "Teclado", 200, 0)

produtos = [p1, p2, p3]

---------------------------------------------------------------------

PARTE 3 — Funcionalidades

1. Listar produtos disponíveis
Crie uma função:
def produtos_disponiveis(lista_produtos):
    # retorna apenas produtos com estoque > 0

--------------------------------------------------

2. Calcular valor total em estoque
def valor_total_estoque(lista_produtos):
    # soma de (preco * estoque) de todos os produtos

--------------------------------------------------

3. Aplicar desconto geral
def aplicar_desconto_geral(lista_produtos, percentual):
    # aplica desconto em todos os produtos

--------------------------------------------------

4. Buscar produto por nome
def buscar_produto(lista_produtos, nome):
    # retorna o produto correspondente ou None

--------------------------------------------------

5. Simular venda
def vender_produto(lista_produtos, codigo, quantidade):

Regras:
- Se o produto não existir → raise ValueError
- Se estoque insuficiente → raise ValueError
- Caso contrário → reduzir estoque

---------------------------------------------------------------------

DESAFIO EXTRA (OPCIONAL)

Criar um menu simples com input:

1 - Listar produtos
2 - Vender produto
3 - Aplicar desconto
4 - Sair

---------------------------------------------------------------------

OBJETIVO FINAL:
Construir um sistema funcional simples, organizado e próximo do mundo real.
"""
