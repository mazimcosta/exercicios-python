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
    try:
        codigo=str(codigo)
        nome=str(nome)
        preco=float(preco)
        disponivel=bool(disponivel)
    except (ValueError,TypeError):
        return "Erro: Dados invalidos"
    cardapio[codigo]={
        'nome':nome,
        'preco':preco,
        'disponivel':disponivel
    }
    return cardapio

def atualizar_preco(cardapio:dict,codigo:str,novo_preco:float):
    if novo_preco<0:
        return f'Erro: preco não pode ser negativo'
    
    try:

      for chave in cardapio.keys():
          if chave==codigo:
              cardapio[chave]['preco']=novo_preco
    except KeyError:
        return False
    return True

def preco_medio(cardapio:dict):
    total=0
    for codigo in cardapio:
        if cardapio[codigo]['disponivel']==True:
             total+=cardapio[codigo]['preco']
    media=total/len(cardapio.keys())
    media=round(media,2)
    return media


    
def buscar_por_faixa(cardapio:dict,minimo:float,maximo:float):
    lista=[cardapio['codigo']['nome'],cardapio['codigo']['preco'] for cardapio in cardapio if cardapio['codigo']['preco']>=minimo
           and cardapio['codigo']['preco']<=maximo]
    return lista

