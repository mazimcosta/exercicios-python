# ======================================
# EXERCÍCIOS - NÍVEL INTERMEDIÁRIO
# ======================================

usuarios = {
    "u1": {"nome": "Ana", "idade": 22, "saldo": 150.0, "ativo": True},
    "u2": {"nome": "Bruno", "idade": 35, "saldo": 0.0, "ativo": False},
    "u3": {"nome": "Carlos", "idade": 28, "saldo": 300.0, "ativo": True},
}


# --------------------------------------
# EXERCÍCIO 1
# --------------------------------------
"""
Retorne uma lista com os nomes de usuários que têm saldo maior que 0.
"""


# --------------------------------------
# EXERCÍCIO 2
# --------------------------------------
"""
Crie uma função sacar(usuarios, codigo, valor)

Regras:
- só pode sacar se o usuário existir
- só pode sacar se saldo >= valor
- diminui o saldo
- retorna True se conseguiu
- retorna False caso contrário
"""


# --------------------------------------
# EXERCÍCIO 3
# --------------------------------------
"""
Crie uma função depositar(usuarios, codigo, valor)

Regras:
- só deposita se o usuário existir
- soma o valor ao saldo
- retorna o novo saldo
- se não existir, retorna -1
"""


# --------------------------------------
# EXERCÍCIO 4
# --------------------------------------
"""
Retorne o saldo TOTAL de todos os usuários ativos.
"""


# --------------------------------------
# EXERCÍCIO 5
# --------------------------------------
"""
Crie uma função desativar_usuarios_zerados(usuarios)

Regras:
- todo usuário com saldo 0 deve ficar com ativo = False
- não retornar nada (apenas modificar o dicionário)
"""


# --------------------------------------
# EXERCÍCIO 6
# --------------------------------------
"""
Crie uma função buscar_usuarios_por_idade(usuarios, idade_min)

Retorne uma lista de usuários com idade >= idade_min
(retorne o dicionário completo de cada um)
"""


# --------------------------------------
# EXERCÍCIO 7
# --------------------------------------
"""
Crie uma função transferir(usuarios, origem, destino, valor)

Regras:
- ambos devem existir
- origem precisa ter saldo suficiente
- debita de um e adiciona no outro
- retorna True se sucesso
- False caso contrário
"""


# --------------------------------------
# EXERCÍCIO 8 (DESAFIO REAL)
# --------------------------------------
"""
Crie uma função usuario_mais_rico(usuarios)

Retorne:
{
    "codigo": "...",
    "dados": {...}
}

Se estiver vazio, retorne {}
"""