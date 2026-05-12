# =============================================================================
# EXERCÍCIO 08 | Dicionários e métodos
# Nível: Médio | Contexto: Cardápio de restaurante
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
''''
CONTEXTO:
Sistema de cardápio digital de um restaurante.
Precisa gerenciar itens, preços e disponibilidade.

TAREFA:
Crie as funções:

- adicionar_item(cardapio: dict, codigo: str,
                  nome: str, preco: float,
                  disponivel: bool = True) -> dict

- atualizar_preco(cardapio: dict, codigo: str,
                   novo_preco: float) -> bool

- itens_disponiveis(cardapio: dict) -> list
  Retorna lista de nomes dos itens disponíveis

- preco_medio(cardapio: dict) -> float
  Calcula média apenas dos itens disponíveis

- buscar_por_faixa(cardapio: dict,
                    minimo: float,
                    maximo: float) -> list
  Retorna itens dentro da faixa de preço

RESTRIÇÕES:
- Usar .get(), .keys(), .values(), .items()
- try/except em atualizar_preco para código inexistente
'''

#SOLUÇÃO:
def adicionar_item(cardapio:dict,codigo:str,nome:str,preco:float,disponivel:bool):
    if nome is not isinstance(nome,str):
        return f'Erro: nome precisa ser um texto'
    if preco<0:
        return f'Erro: preco não pode ser negativo'
    elif preco is not isinstance(preco,(int,float)):
        return f' preco invalido'
    if disponivel not in [True,False]:
        return f'Erro:disponibilidade errada'
    
    cardapio[codigo]={
        'nome':nome,
        'preco':preco,
        'disponibilidade':disponivel

    }
    return cardapio

def atualizar_preco(cardapio:dict,codigo:str,novo_preco:float):
    if novo_preco<0:
        return False
    try:
        cardapio[codigo]['preco']=float(novo_preco)
        return True
    except KeyError:
        return False

def itens_disponiveis(cardapio:dict):
    lista=[]
    for item in cardapio.values():
        if item['disponivel']==True:
            lista.append(item['nome'])
        if not lista:
            return f'Não ha itens disponiveis'
    return lista

def preco_medio(cardapio:dict):
    lista=[]
    media=0
    for item in cardapio.items():
        if item['disponivel']==True:
            lista.append(item['preco'])
    try:
        media=sum(lista)/len(lista)
        media=round(media,2)
        return media
    except ZeroDivisionError:
        return f' Não ha itens disponiveis'
    
def buscar_por_faixa(cardapio:dict,minimo:float,maximo:float):
    lista=[{'nome':item['nome'],'preco':item['preco']} for item in cardapio.items() if minimo<=item['preco']<=maximo]
    return lista

itens=[('456','feijoada',45.8,True),
       ('4512','macarronada',25.2,False),
       ('8795','pastelao',52.3,True)]

for codigo,nome,preco,disponivel in itens:
    cardapio=adicionar_item(codigo=codigo,nome=nome,preco=preco,disponivel=disponivel)

print(cardapio)

    

