# ================================
# EXERCÍCIOS - LISTAS E DICIONÁRIOS
# ================================




# --------------------------------
# EXERCÍCIO 1
# --------------------------------
"""
Percorra o dicionário 'dados' e imprima:
- o código (chave)
- o nome
- a idade

Saída esperada (exemplo):
1 João 25
2 Maria 30
3 Pedro 20
"""
dados = {
    "1": {"nome": "João", "idade": 25, "ativo": True},
    "2": {"nome": "Maria", "idade": 30, "ativo": False},
    "3": {"nome": "Pedro", "idade": 20, "ativo": True}
}


for codigo,dados in dados.items():
    print(codigo,dados['nome'],dados['idade'],sep='\n')








# --------------------------------
# EXERCÍCIO 2
# --------------------------------
"""
Crie uma função chamada buscar_pessoa(dados, codigo)

Ela deve:
- retornar o dicionário da pessoa se existir
- retornar {} se não existir

Use .get()

"""
def buscar_pessoas(dados,codigo):

    item=dados.get(codigo)
    if item is not None:
        return dados[codigo]
    return {}








# --------------------------------
# EXERCÍCIO 3
# --------------------------------
"""
Crie uma função chamada pessoa_existe(dados, codigo)

Ela deve:
- retornar True se o código existir
- retornar False caso contrário

Use 'in' (não use .get aqui)
"""
def  pessoa_existe(dados,codigo):
    if codigo in dados:
        return True
    return False

# --------------------------------
# EXERCÍCIO 4
# --------------------------------
"""
Crie uma função chamada atualizar_idade(dados, codigo, nova_idade)

Ela deve:
- atualizar a idade da pessoa
- retornar True se conseguiu atualizar
- retornar False se o código não existir
"""
def atualizar_idade(dados,codigo,nova_idade):
    try:
        dados[codigo]['idade']=int(nova_idade)
        return True
    except(KeyError,ValueError):
        return False







# --------------------------------
# EXERCÍCIO 5
# --------------------------------
"""
Crie uma função chamada remover_pessoa(dados, codigo)

Ela deve:
- remover a pessoa do dicionário
- retornar True se removeu
- retornar False se o código não existir
"""


# --------------------------------
# EXERCÍCIO 6
# --------------------------------
"""
Calcule a média de idade das pessoas.

Dica:
- percorra usando .values()
- use um acumulador (soma)
"""


# --------------------------------
# EXERCÍCIO 7
# --------------------------------
"""
Crie uma função chamada listar_ativos(dados)

Ela deve:
- retornar uma lista com os nomes das pessoas que estão ativas (ativo = True)

Exemplo de saída:
["João", "Pedro"]
"""


# --------------------------------
# EXERCÍCIO 8
# --------------------------------
"""
Crie uma função chamada contar_inativos(dados)

Ela deve:
- contar quantas pessoas estão com ativo = False
- retornar esse número
"""


# --------------------------------
# EXERCÍCIO 9
# --------------------------------
"""
Crie uma função chamada alternar_status(dados, codigo)

Ela deve:
- inverter o status 'ativo' (True vira False, False vira True)
- retornar True se conseguiu
- retornar False se o código não existir
"""


# --------------------------------
# EXERCÍCIO 10 (DESAFIO)
# --------------------------------
"""
Crie uma função chamada adicionar_pessoa(dados, codigo, nome, idade)

Ela deve:
- adicionar uma nova pessoa no dicionário
- não permitir códigos duplicados
- retornar True se adicionou
- retornar False se o código já existir
"""


# ================================
# FIM DOS EXERCÍCIOS
# ================================
