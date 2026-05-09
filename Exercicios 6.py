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
        dado=str(dado)
        if dado is None:
            return{'sucess':False,'motivo':'valor invalido'}
        linhas+=dado.count('\n')
        return {'sucess':True,'resultado':linhas}
    
    if fonte=='numero':
        try:
            dado=float(dado)
        except ValueError:
            return {'sucess':False,'motivo':'valor invaido'}
        
        try:
            raiz=math.sqrt(dado)
        except ValueError:
            return {'sucess':False,'motivo':'raiz inexistente'}
        
        return {'sucess':True,'resultado':round(raiz,2)}

    if fonte=='lista':
        try:
            indice=dado[0]
        except IndexError:
            return {'sucess':False,'motivo':'Valor não pode ser acessado'}
        return {'sucess':True,'resultado':indice}
    
    if fonte=='dicionario':
        if not dado.get['valor','preco']:
            return {'sucess':False,'motivo':'valor ou preco invaido'}
        else:
            return {'sucess':True,'resultado':dado.get['valor','preco']}

resultado_final={}
for fonte,dado in testes:
    resultado_final=importar_dado(fonte,dado)

print(resultado_final)


