# =============================================================================
# EXERCÍCIO 14 | Listas de objetos
# Nível: Médio-Difícil | Contexto: Gestão de funcionários
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de RH que gerencia uma lista de funcionários.

TAREFA:
Crie a classe Funcionario e a classe Departamento:

Funcionario:
- nome, cargo, salario, anos_empresa
- calcular_bonus() → 5% por ano de empresa, máximo 30%
- __str__()

Departamento:
- nome, lista de funcionários
- adicionar(funcionario: Funcionario)
- remover(nome: str) -> bool
- maior_salario() -> Funcionario
- menor_salario() -> Funcionario
- media_salarial() -> float
- relatorio() -> str  (relatório completo formatado)
- __len__() → quantidade de funcionários

RESTRIÇÕES:
- Funções de busca usando for dentro dos métodos
- try/except em remover
- __len__ obrigatório
"""
# SUA SOLUÇÃO:


class Funcionario:

    def __init__(self,nome,cargo,salario,anos_empresa):
        if not isinstance(nome,str):
            raise ValueError('Nome invalido')
        elif not nome.strip().replace(' ','').isalpha():
            raise ValueError('Nome invalido')
        elif not isinstance(cargo,str):
            raise ValueError('Cargo invalido')
        elif not cargo.strip().replace(' ','').isalpha():
            raise ValueError('Cargo invalido')
        elif not isinstance(salario,(int,float)):
            raise ValueError('Salario invalido')
        elif salario<=0:
            raise ValueError('Salario invalido')
        elif not isinstance(anos_empresa,int):
            raise ValueError('Anos de empresa invalido')
        elif anos_empresa<0:
            raise('Anos de empresa nao pode ser negqtivo')
        self.nome=nome
        self.cargo=cargo
        self.salario=salario
        self.anos_empresa=anos_empresa

    def calcular_bonus(self):
        if self.anos_empresa==0:
            bonus=0
        elif self.anos_empresa<6:
            bonus=round((self.salario *(0.05*self.anos_empresa)),2)
        else:
            bonus= round(self.salario * 0.3,2)
        return bonus
    
    def __str__(self):
        return f' Funcionario(nome:{self.nome} cargo:{self.cargo} salario:{self.salario}, anos de empresa: {self.anos_empresa})'