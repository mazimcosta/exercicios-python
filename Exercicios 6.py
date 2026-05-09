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
    variavel_auxiliar=''
    qtd_linhas=0
    resultado={}
        
    if fonte.lower()=='arquivo':
        try:
            dado=str(dado)
        except TypeError:
            return resultado.update({'fonte':fonte,'dado':dado,'sucess':False,'motivo':'Valor invalido'})

        for letra in dado:
            if letra in ["\'",'n']:
                variavel_auxiliar+=letra
                if variavel_auxiliar=="\n":
                    qtd_linhas+=1
                    variavel_auxiliar=''
        resultado.update({'fonte':fonte,'dado':dado,'sucess':True,'quantidade de linhas':qtd_linhas})

        if fonte.lower()=='numero':
            try:
                dado=float(dado)
                raiz=math.sqrt(dado)
            except ValueError:
                return resultado.update({'fonte':fonte,'dado':dado,'sucess':False,'motivo':'Valor invalido.'})
            resultado.update({'fonte':fonte,'dado':dado,'sucess':True,'resultado':raiz})

        if fonte.lower()=='lista':
            try:
                indice=dado[0]
            except IndexError:
                resultado.update({'fonte':fonte,'dado':dado,'sucess':False,'motivo':'Valor invalido.'})
            resultado.update({'fonte':fonte,'dado':dado,'sucess':True,'resutado':indice})

        if fonte.lower()=='dicionario':
            try:
                for chave,valor in dado:
                    key=chave
                    value=valor
            except IndexError:
                resultado.update({'fonte':fonte,'dado':dado,'sucess':False,'motivo':'valor invalido.'})
            resultado.update({'fonte':fonte,'dado':dado,'sucess':True,'resultado':f'{key=},{value=}'})
        
        return resultado
    

for fonte,dado in testes:
    resultado_final=importar_dado(fonte,dado)

print(resultado_final)


        

