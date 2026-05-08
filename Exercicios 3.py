# =============================================================================
# EXERCÍCIO 03 | Estruturas condicionais
# Nível: Médio | Contexto: Sistema de RH
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de RH precisa calcular o imposto de renda
e o bônus anual de cada funcionário.

TAREFA:
Crie a função calcular_beneficios(salario: float,
                                   anos_empresa: int,
                                   cargo: str) -> dict que retorne:
- imposto: baseado na tabela abaixo
- bonus: baseado nas regras abaixo
- salario_liquido: salario - imposto + bonus

TABELA DE IMPOSTO:
- Até R$2.000      → isento
- R$2.001 a R$3.000 → 7.5%
- R$3.001 a R$4.500 → 15%
- R$4.501 a R$6.000 → 22.5%
- Acima de R$6.000  → 27.5%

REGRAS DE BÔNUS MENSAL:
- Gerente + 5 anos → 20% do salário
- Gerente          → 15% do salário
- Analista + 3 anos → 10% do salário
- Analista         → 5% do salário
- Outros           → sem bônus

RESTRIÇÕES:
- if/elif/else obrigatório
- Sem dicionário de tabela — use condicionais puras
- Arredondar para 2 casas decimais
"""
# SUA SOLUÇÃO:

funcionarios = [
    {"nome": "Ana Paula",     "cargo": "Gerente",  "salario": 8500.00, "anos_empresa": 7},
    {"nome": "Carlos Lima",   "cargo": "Analista", "salario": 4200.00, "anos_empresa": 3},
    {"nome": "Beatriz Costa", "cargo": "Gerente",  "salario": 9200.00, "anos_empresa": 2},
    {"nome": "Pedro Souza",   "cargo": "Analista", "salario": 3800.00, "anos_empresa": 1},
    {"nome": "Julia Rocha",   "cargo": "Gerente",  "salario": 7600.00, "anos_empresa": 6},
    {"nome": "Marcos Silva",  "cargo": "Analista", "salario": 5100.00, "anos_empresa": 4},
    {"nome": "Fernanda Lima", "cargo": "Estagio",  "salario": 1800.00, "anos_empresa": 0},
    {"nome": "Rafael Dias",   "cargo": "Estagio",  "salario": 1500.00, "anos_empresa": 1},
]

calculo_beneficios=list()
def calcular_beneficios(nome:str,salario:float,cargo:str,anos_empresa:int):
        resultado=dict()

        try:
            salario=float(salario)
            cargo=str(cargo).lower().strip()
            anos_empresa=int(anos_empresa)
        except (ValueError,TypeError):
            return f'"nome":{nome} erros: dados invalidos'

        if salario<=2000:
            imposto=0

        elif salario<=3000:
            imposto=round(0.075 *salario,2)

        elif salario <=4500:
            imposto=round(salario * 0.15,2)
        
        elif salario<=6000:
            imposto=round(0.225 *salario,2)

        else:
            imposto=round(0.275 *salario,2)
        
        if cargo=='gerente' and anos_empresa>5:
            bonus=round(0.2 * salario,2)
        elif cargo=='gerente':
            bonus=round(0.15 * salario,2)
        elif cargo=='analista' and anos_empresa>3:
            bonus=round(0.1 * salario,2)
        elif cargo=='analista':
            bonus=round(0.05 * salario,2)
        else:
            bonus=0
        salario_liquido=round(salario - imposto + bonus,2)
        
        resultado.update({'nome':nome,'imposto':imposto,'bonus':bonus,'salario_liquido':salario_liquido})
        return resultado

for funcionario in funcionarios:
    resultado=calcular_beneficios(funcionario['nome'],funcionario['salario'],funcionario['cargo'],funcionario['anos_empresa'])
    calculo_beneficios.append(resultado)
     


print(calculo_beneficios)  
    
