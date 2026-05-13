"Crie uma função que retorna o usuário ativo com MENOR saldo."

# Regras:
# - considerar apenas usuários com ativo = True
# - se não houver usuários ativos, retornar None
# - retornar no formato:
# {
#     'codigo': ...,
#     'dados': {...}
# }
# "

def menor_saldo(usuarios,codigo):
    if usuarios[codigo]['ativo']:
        lista=[(codigo,dados) for codigo,dados in usuarios.items()]
        minimo=min(lista, key= lambda item:item[1]['saldo'])
        return {'codigo':minimo[0],'dados':minimo[1]}
    return None
