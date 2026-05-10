# =============================================================================
# EXERCÍCIO 06 | try/except com múltiplos erros
# Nível: Médio | Contexto: Importação de dados externos
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema que importa dados de várias fontes externas.
Cada fonte pode falhar de formas diferentes.

TAREFA:
Crie a função importar_dado(fonte: str, dado: any) -> dict que:
- "arquivo": tente converter dado para string e contar linhas
- "numero": tente converter para float e calcular raiz quadrada
- "lista": tente acessar o índice 0 do dado
- "dicionario": tente acessar a chave "valor" do dado
- Capture cada tipo de erro específico
- Retorne {"sucesso": True/False, "resultado": ..., "erro": ...}

RESTRIÇÕES:
- try/except separado para cada tipo de erro
- Capturar TypeError, ValueError, IndexError, KeyError
- Nunca usar except Exception genérico
"""

# =========================
# TODOS OS TESTES JUNTOS
# =========================
import math


testes = [
    ("arquivo", "linha 1\nlinha 2\nlinha 3"),
    ("arquivo", None),

    ("numero", "25"),
    ("numero", "abc"),
    ("numero", "-9"),

    ("lista", [10, 20, 30]),
    ("lista", []),

    ("dicionario", {"valor": 150}),
    ("dicionario", {"preco": 100}),
]


def importar_dado(fonte:str,dado:any):
    
    linhas=0
    if fonte=='arquivo':
        
        if dado is None:
            return{'sucesso':False,'resultado':None,'erro':'Valor invalido.'}
        dado=str(dado)
        linhas+=dado.count('\n')
        return {'sucesso':True,'resultado':linhas,'erro':None}
    
    if fonte=='numero':
        try:
            dado=float(dado)
        except ValueError:
            return {'sucesso':False,'resultado':None,'erro':'Valor invalido.'}
        
        try:
            raiz=math.sqrt(dado)
        except ValueError:
            return {'sucesso':False,'resultado':None,'erro':'Valor invalido.'}
        
        return {'sucesso':True,'resultado':round(raiz,2),'erro':None}

    if fonte=='lista':
        try:
            indice=dado[0]
        except IndexError:
            return {'sucesso':False,'resultado':None,'erro':'Valor invalido.'}
        return {'sucesso':True,'resultado':indice,'erro':None}
    
    if fonte=='dicionario':
        try:
            dado['valor']
        except KeyError:
            return{'sucesso':False,'resultado':None,'erro':'Valor invalido.'}
        return{'sucesso':True,'resultado':dado['valor'],'erro':None}

resultado_final={}
for fonte,dado in testes:
    resultado_final=importar_dado(fonte,dado)

print(resultado_final)


