#Exercicio 19

'''TAREFA:
Crie as funções:

- calcular_comissao(vendas: float, cargo: str) -> float
  Tabela de comissão:
  "Junior"  → 2% até R$10k, 3% acima
  "Pleno"   → 3% até R$15k, 5% acima
  "Senior"  → 5% até R$20k, 8% acima

- gerar_ranking(vendedores: list) -> list
  → ordena por total de vendas (decrescente)
  → adiciona posição, comissão e medalha:
    1º → "🥇", 2º → "🥈", 3º → "🥉", resto → ""

- resumo_ranking(ranking: list) -> str
  → retorna relatório formatado com top 3 destacado'''

vendedores = [
    {"nome": "Ana",    "cargo": "Senior", "vendas": 22000.0},
    {"nome": "Carlos", "cargo": "Pleno",  "vendas": 18000.0},
    {"nome": "Pedro",  "cargo": "Junior", "vendas": 9500.0},
    {"nome": "Julia",  "cargo": "Senior", "vendas": 31000.0},
    {"nome": "Marcos", "cargo": "Pleno",  "vendas": 12000.0},
]

