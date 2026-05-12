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
lista=[{'nome':usuario['nome']} for usuario in usuarios.values() if usuario['saldo']>0]




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
def sacar(usuarios,codigo,valor):
    if codigo in usuarios:
        if usuarios[codigo]['saldo']>=valor:
            usuarios[codigo]['saldo']-=valor
        return True
    return False


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
def depositar(usuarios,codigo,valor):
    if valor<0:
        return f'Valor invalido'
    if usuarios.get(codigo) is not None:
        usuarios[codigo]['saldo']+=valor
        return f"novo saldo: {usuarios[codigo]['saldo']}"
    return -1











# --------------------------------------
# EXERCÍCIO 4
# --------------------------------------
"""
Retorne o saldo TOTAL de todos os usuários ativos.
"""
def calcular_total(usuarios,total):
    total=0
    for usuario in usuarios.values():
        if usuario['ativo']==True:
            total+=usuario['saldo']

        return f'saldo total: {total:.2f}'







# --------------------------------------
# EXERCÍCIO 5
# --------------------------------------
"""
Crie uma função desativar_usuarios_zerados(usuarios)

Regras:
- todo usuário com saldo 0 deve ficar com ativo = False
- não retornar nada (apenas modificar o dicionário)
"""
def desativar_usuarios_zerados(usuarios):
    for usuario in usuarios.values():
        if usuario['saldo']==0:
            usuario['ativo']=False
    
    return 









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