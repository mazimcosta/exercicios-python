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
def calcular_comissao(vendas, cargo):
    cargo = cargo.lower()

    if cargo == "junior":
        percentual = 0.02 if vendas <= 10000 else 0.03

    elif cargo == "pleno":
        percentual = 0.03 if vendas <= 15000 else 0.05

    elif cargo == "senior":
        percentual = 0.05 if vendas <= 20000 else 0.08

    else:
        raise ValueError("Cargo invalido")

    return round(vendas * percentual, 2)


def gerar_ranking(vendedores):
    ordenados = sorted(vendedores, key=lambda item: item["vendas"], reverse=True)

    ranking = []

    for i, vendedor in enumerate(ordenados, start=1):
        medalha = ""

        if i == 1:
            medalha = "🥇"
        elif i == 2:
            medalha = "🥈"
        elif i == 3:
            medalha = "🥉"

        ranking.append({
            "posicao": i,
            "medalha": medalha,
            "nome": vendedor["nome"],
            "cargo": vendedor["cargo"],
            "vendas": vendedor["vendas"],
            "comissao": calcular_comissao(vendedor["vendas"], vendedor["cargo"])
        })

    return ranking


def resumo_ranking(ranking):
    linhas = []
    linhas.append("=" * 40)
    linhas.append("RANKING DE VENDAS")
    linhas.append("=" * 40)

    for item in ranking:
        linhas.append(
            f'{item["posicao"]}º {item["medalha"]} '
            f'{item["nome"]} | Cargo: {item["cargo"]} | '
            f'Vendas: R${item["vendas"]:.2f} | '
            f'Comissão: R${item["comissao"]:.2f}'
        )

    return "\n".join(linhas)            