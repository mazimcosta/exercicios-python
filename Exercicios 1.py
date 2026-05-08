
# =============================================================================
# EXERCÍCIO 01 | Tipos de dados e conversão
# Nível: Médio | Contexto: Sistema financeiro
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Você recebeu dados de um formulário onde tudo chega como string.
Precisa converter e validar antes de processar.

TAREFA:
Crie a função processar_formulario(dados: dict) -> dict que:
- Converta "idade" para int
- Converta "saldo" e "limite" para float
- Converta "ativo" para bool ("true"/"false" → True/False)
- Retorne os dados convertidos ou erro por campo se falhar

ENTRADA:
dados = {
    "nome": "Ana Silva",
    "idade": "28",
    "saldo": "1500.50",
    "limite": "dois mil",
    "ativo": "true"
}

SAÍDA ESPERADA:
{
    "nome": "Ana Silva",
    "idade": 28,
    "saldo": 1500.50,
    "limite": "ERRO: valor inválido",
    "ativo": True
}

RESTRIÇÕES:
- try/except obrigatório por campo
- Sem biblioteca externa
"""


#ENTRADA:
dados = {
    "nome": "Ana Silva",
    "idade": "28",
    "saldo": "1500.50",
    "limite": "dois mil",
    "ativo": "true"
}

def processar_formulario(dados):
    relatorio=dict()
    erro_padrao='Erro: valor invalido'

    
    relatorio['nome']=dados['nome']

    try:
            relatorio['idade']=int(dados['idade'])
    except ValueError:
            relatorio['idade']=erro_padrao

    try:
            relatorio['saldo']=float(dados['saldo'])
        
    except ValueError:
            relatorio['saldo']=erro_padrao


    try:
            relatorio['limite']=float(dados['limite'])


    except ValueError:
            relatorio['limite']=erro_padrao
        
    if dados['ativo'].lower()=='true':
            relatorio['ativo']=True


    elif dados['ativo'].lower()=='false':
            relatorio['ativo']= False


    else:
            relatorio['ativo']= erro_padrao
    
    return relatorio