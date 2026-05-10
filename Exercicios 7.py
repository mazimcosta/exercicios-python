# =============================================================================
# EXERCÍCIO 07 | Listas e métodos
# Nível: Médio | Contexto: Fila de atendimento
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de fila de atendimento de um banco.
Clientes entram e saem da fila o tempo todo.

TAREFA:
Crie as funções abaixo para gerenciar a fila:

- entrar_fila(fila: list, cliente: str, preferencial: bool) -> list
  Se preferencial, insere na posição 0. Senão, no final.

- chamar_proximo(fila: list) -> str
  Remove e retorna o primeiro da fila.
  Se vazia, retorna "Fila vazia"

- cancelar_senha(fila: list, cliente: str) -> bool
  Remove cliente da fila se existir. Retorna True/False.

- posicao_na_fila(fila: list, cliente: str) -> int
  Retorna a posição (1-based). -1 se não encontrar.

- status_fila(fila: list) -> dict
  Retorna total, primeiro da fila e último da fila.

RESTRIÇÕES:
- Usar métodos de lista: append, insert, pop, remove, index
- try/except em cancelar_senha e posicao_na_fila
"""
# SUA SOLUÇÃO:
def entrar_fila(lista:list,cliente:str,preferencial:bool):
    lista=[]
    if preferencial==True:
        lista.insert(0,cliente)
    else:
        lista.insert(-1,cliente)
    
    return lista
    

def chamar_proximo(fila:list):
    try:
        proximo=fila[0]
        fila.pop(0)
        return f' ultimo chamado: {proximo}'
    except IndexError:
        return f' fIla vazia.'
    

def cancelar_senha(fila,cliente):
    if cliente in fila:
        fila.remove(cliente)
    else:
        return (cliente in fila)    
    return True


def posicao_na_fila(fila:list,cliente):
    try:
        posicao=fila.index(cliente)
    except :
        return -1
    return f'posicao  do {cliente} e {posicao}'

def status_fila(fila:list):
    try:
      status={'total':len(fila),'primeiro da fila':fila[0],'ultimo da fila':fila[-1]}
    except:
        return f' a fila esta vazia'
    return status


        
