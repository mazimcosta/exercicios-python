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

def calcular_saldo_total(usuarios,codigo):
    saldo_total=0
    for codigo in usuarios:
        if usuarios[codigo]['ativo']==True:
            saldo_total+=usuarios[codigo]['saldo']
        
    return  saldo_total








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
    lista=list()
    lista=lista.sort(usuarios, key= lambda k:usuarios[k]['saldo'], reverse=True)
    return lista