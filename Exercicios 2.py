"""
CONTEXTO:
O sistema bancário recebe dados em formato fixo de string.
Você precisa extrair as informações por posição.

TAREFA:
Crie a função extrair_dados_bancarios(linha: str) -> dict que
extraia os campos pelo fatiamento da string.

FORMATO DA STRING (posições fixas):
- 0:10   → data (ex: "2024-03-01")
- 10:21  → agência (ex: "  0001-5  ")
- 21:36  → conta (ex: " 12345-6     ")
- 36:50  → valor (ex: "      1500.00")
- 50:51  → tipo ("C" = crédito, "D" = débito)

ENTRADA:
"2024-03-01  0001-5   12345-6        1500.00C"

SAÍDA ESPERADA:
{
    "data": "2024-03-01",
    "agencia": "0001-5",
    "conta": "12345-6",
    "valor": 1500.00,
    "tipo": "crédito"
}

RESTRIÇÕES:
- Usar apenas fatiamento de string
- strip() para limpar espaços
- try/except na conversão do valor
"""
# SUA SOLUÇÃO:

# A len(entrada) não tem range(51) como exemplifica a questão então usarei for para obter os iteraveis de cada string:

def debug_indices(entrada):
    for i in range(0,len(entrada)):
     print(i,entrada[i])

#data[0:10],agencia[12:18],conta[21:28],valor[36:43],tipo[43]

def extrair_dados_bancarios(linha):
    dados=dict()
    dados['data']=linha[0:10].strip()
    dados['agencia']=linha[12:18].strip()
    dados['conta']=linha[21:28].strip()

    try:
        dados['valor']=float(linha[36:43])
    except ValueError:
        dados['valor']='Erro: Valor invalido'

    if linha[43].lower()=='c':
        dados['tipo']='crédito'
    elif linha[43].lower()=='d':
        dados['tipo']='débito'
    else:
        dados['tipo']='Erro:Valor invalido'
    return dados

entrada='2024-03-01  0001-5   12345-6        1500.00C'
dados=extrair_dados_bancarios(entrada)
print(dados)