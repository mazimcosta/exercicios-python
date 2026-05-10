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
def entrar_fila(fila:list,cliente:str,preferencial:bool):
    lista=[]
    if preferencial==True:
        fila.insert(0,cliente)
    else:
        fila.append(cliente)
    
    return fila
    

def chamar_proximo(fila:list):
    if not fila:
        return 'a fila esta vazia'
    return fila.pop(0)
    

def cancelar_senha(fila,cliente):
    if cliente in fila:
        fila.remove(cliente)
        return True
    else:
        return False


def posicao_na_fila(fila:list,cliente):
    try:
        posicao=fila.index(cliente)
    except  ValueError:
        return -1
    return f' posicao :{posicao +1}'

def status_fila(fila:list):
    try:
      status={'total':len(fila),'primeiro da fila':fila[0],'ultimo da fila':fila[-1]}
    except IndexError:
        return {'total':0,'primeiro da fila':None,'ultimo da fila':None}
    return status


        
