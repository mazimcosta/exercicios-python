# ======================================
# EXERCÍCIOS - NÍVEL INTERMEDIÁRIO
# ======================================

usuarios = {
    "u1": {"nome": "Ana", "idade": 22, "saldo": 150.0, "ativo": True},
    "u2": {"nome": "Bruno", "idade": 35, "saldo": 0.0, "ativo": False},
    "u3": {"nome": "Carlos", "idade": 28, "saldo": 300.0, "ativo": True},
}
# EXERCÍCIO 12
"Crie uma função que retorna o saldo total de todos os usuários ativos."

def calcular_saldo(usuarios):
    saldo_total=0
    for dados in usuarios.values():
        if dados['ativo']:
            saldo_total+=dados['saldo']
    
    return saldo_total







# EXERCÍCIO 13
"Crie uma função que retorna o usuário mais jovem."

def mais_jovem(usuarios):

    codigo=min(usuarios,key= lambda k:usuarios[k]['idade'])

    return{'codigo':codigo,'dados':usuarios[codigo]}















# EXERCÍCIO 14
"Crie uma função que desativa usuários com saldo zero."
def desativar_usuarios(usuarios):
    for dados in usuarios.values():
        if dados['saldo']==0:
            dados['ativo']=False
    return








# EXERCÍCIO 15 (DESAFIO)
"Crie uma função que retorna uma lista ordenada de usuários por saldo (do maior para o menor)."

def ordenar_usuarios(usuarios):
    return sorted(usuarios.items(), key= lambda item:item[1]['saldo'], reverse=True)

    "Crie uma função que retorna apenas os usuários ativos ordenados por saldo"

    def ordenar_ativos(usuarios):
        for dados in usuarios.values:
            if dados['ativo']:
                return sorted(dados, key= lambda k:k['saldo'])