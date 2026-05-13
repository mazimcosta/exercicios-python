# ======================================
# EXERCÍCIOS - NÍVEL INTERMEDIÁRIO
# ======================================

usuarios = {
    "u1": {"nome": "Ana", "idade": 22, "saldo": 150.0, "ativo": True},
    "u2": {"nome": "Bruno", "idade": 35, "saldo": 0.0, "ativo": False},
    "u3": {"nome": "Carlos", "idade": 28, "saldo": 300.0, "ativo": True},
}

# --------------------------------------
# EXERCÍCIO 6
# --------------------------------------
"""
Crie uma função buscar_usuarios_por_idade(usuarios, idade_min)

Retorne uma lista de usuários com idade >= idade_min
(retorne o dicionário completo de cada um)
"""
def buscar_usuarios_por_idade(usuarios,idade_min):
    lista=[{codigo,dados}for codigo,dados in usuarios.items() if dados['idade']>=idade_min]

    return lista





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
def transferir(usuarios,origem,destino,valor):
    # Assumindo que origem e destino são chaves:
    if origem in usuarios and destino in usuarios and usuarios[origem]['saldo']>=valor:
        usuarios[origem]['saldo']-=valor
        usuarios[destino]['saldo']+=valor
        return True
    return False












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
def usuario_mais_rico(usuarios):
    lista=list()
    lista=[{codigo,dados} for codigo,dados in usuarios.items()]
    lista=lista.sort(key= lambda item:item['saldo'])

    return{'codigo':lista[-1][0],
           'dados':lista[-1][1]}