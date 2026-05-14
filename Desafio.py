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

# ================================
# 🛒 MINI PROJETO: SISTEMA DE CARRINHO
# ================================

# 🎯 OBJETIVO:
# Criar um sistema simples de loja com:
# - Produtos
# - Carrinho de compras
# - Controle de estoque
# - Cálculo de total


# =====================================
# 📦 PARTE 1 — CLASSE PRODUTO
# =====================================

# Crie uma classe Produto com os seguintes requisitos:

# Atributos:
# - codigo (str)
# - nome (str)
# - preco (float) → usar @property com validação (não pode ser negativo)
# - estoque (int) → usar validação (não pode ser negativo)

# Métodos:
# - aplicar_desconto(percentual: float)
#     → reduz o preço com base no percentual

# - adicionar_estoque(qtd: int)
#     → aumenta o estoque

# - remover_estoque(qtd: int)
#     → diminui o estoque
#     → levantar erro se não houver estoque suficiente

# - esta_disponivel() -> bool
#     → retorna True se estoque > 0

# - valor_em_estoque() -> float
#     → retorna preco * estoque

# - __str__()
#     → representação amigável do produto

# - __repr__()
#     → representação técnica


# =====================================
# 🛒 PARTE 2 — CLASSE CARRINHO
# =====================================

# Crie uma classe Carrinho com:

# Atributos:
# - itens (lista de produtos)

# Métodos:

# - adicionar(produto)
#     → adiciona produto ao carrinho
#     → só adiciona se houver estoque
#     → deve remover 1 unidade do estoque

# - remover(codigo)
#     → remove produto do carrinho pelo código

# - listar()
#     → mostra todos os produtos do carrinho

# - total()
#     → retorna o valor total da compra

# - finalizar_compra()
#     → mostra o total final
#     → limpa o carrinho


# =====================================
# 🧪 PARTE 3 — TESTE DO SISTEMA
# =====================================

# Crie alguns produtos manualmente, exemplo:
# - arroz
# - macarrão
# - leite

# Depois:

# 1. Crie um carrinho
# 2. Adicione produtos
# 3. Liste os itens
# 4. Mostre o total
# 5. Finalize a compra


# =====================================
# 🔥 DESAFIOS EXTRAS (OPCIONAL)
# =====================================

# - Não permitir adicionar produto sem estoque
# - Mostrar mensagem ao tentar remover produto inexistente
# - Aplicar desconto em todos os produtos do carrinho
# - Mostrar quantidade de itens no carrinho


# =====================================
# 🚀 OBJETIVO FINAL
# =====================================

# Quando terminar, seu sistema deve:
# - Controlar estoque corretamente
# - Calcular valores corretamente
# - Usar bem classes e métodos
# - Estar organizado e legível

# 👉 Depois me manda que eu reviso como se fosse código profissional.
