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
    erros=list()
    cardapio={}
    if not isinstance(nome,str):
        erros.append(('Erro: nome precisa ser um texto'))
    if preco<0:
        erros.append(('Erro: o preco nao pode ser negativo'))

    try:
        preco=round(float(preco),2)
        codigo=str(codigo)
        disponivel=bool(disponivel)
    except (ValueError,TypeError):
        erros.append('Erro: Dados invalidos.')

    if erros:
        return erros

    if not erros:
        cardapio.update({'codigo':codigo,'nome':nome,'preco':preco,'disponivel':disponivel})
    return cardapio


def atualizar_preco(cardapio:dict,codigo:str,novo_preco:float):
        
    try:
        if cardapio.get('codigo')==codigo:
            cardapio['preco']=novo_preco
    except KeyError:
        return False
    return True

def itens_disponiveis(cardapio:dict):
    lista=[]
    for nome in cardapio.keys():
        lista.append(nome)
    return lista

def preco_medio(cardapio:dict):
    media=0
    total=0
    for chave,valor in cardapio.items():
        if chave=='preco':
            total+=valor
    
    try:
        media=total/len(cardapio)
        media=float(media)
        media=round(media,2)

    except (ValueError,TypeError):
        return f'Erro:valor invalido'
    
    return media

def buscar_por_faixa(cardapio:dict,minimo:float,maximo:float):
    lista=[]
    
    try:
        minimo=round(float(minimo),2)
        maximo=round(float(maximo),2)
    except (ValueError,TypeError):
        return 'Erro: Valor invalido'
          
    
    for item in cardapio.items():
        if item['preco']>=minimo and item['preco']<=maximo:
           lista.append(item['nome'],item['preco'])

    return lista 