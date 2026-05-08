# =============================================================================
# 25 EXERCÍCIOS COMPLETOS — REVISÃO GERAL FASE 1
# Cobre: tipos, strings, conversão, if/else, while, for, try/except,
#        listas, dicionários, funções, sets, classes e métodos
# Nível: Médio a Difícil — contexto real de mercado
# Regra: 1 exercício por dia | Enviar para revisão antes de avançar
# =============================================================================


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
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 02 | Fatiamento de strings
# Nível: Médio | Contexto: Processamento de dados bancários
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
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


# =============================================================================
# EXERCÍCIO 04 | Loop while com break
# Nível: Médio | Contexto: Sistema de tentativas de pagamento
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de pagamento que tenta processar a transação
até 3 vezes antes de cancelar.

TAREFA:
Crie a função tentar_pagamento(valor: float,
                                saldo: float) -> dict que:
- Simule 3 tentativas de pagamento
- Em cada tentativa, verifique se saldo >= valor
- Se aprovado: retorna sucesso e tentativa em que aprovou
- Se 3 falhas: retorna cancelado
- A cada tentativa falha, o saldo aumenta 10%
  (simulando recarga automática)
- Use while com break

ENTRADA:
valor = 500.00
saldo = 350.00  (insuficiente na 1ª, mas aumenta 10% a cada falha)

SAÍDA ESPERADA (se aprovar na 2ª tentativa):
{
    "status": "APROVADO",
    "tentativa": 2,
    "saldo_final": 385.00,
    "valor_pago": 500.00
}

RESTRIÇÕES:
- while obrigatório com break para sair ao aprovar
- Não use for
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 05 | Loop for com listas
# Nível: Médio | Contexto: Processamento de notas fiscais
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema fiscal que processa uma lista de itens de nota
e calcula os impostos de cada um.

TAREFA:
Crie a função processar_nota_fiscal(itens: list) -> dict que:
- Itere sobre os itens com for
- Calcule o valor total de cada item (qtd * preco)
- Aplique o imposto de acordo com a categoria:
    "Eletrônicos" → 15%
    "Alimentos"   → 7%
    "Vestuário"   → 12%
    Outros        → 10%
- Retorne resumo com total bruto, total impostos e total líquido

ENTRADA:
itens = [
    {"produto": "Notebook", "categoria": "Eletrônicos",
     "qtd": 2, "preco": 3500.00},
    {"produto": "Arroz",    "categoria": "Alimentos",
     "qtd": 10, "preco": 25.90},
    {"produto": "Camiseta", "categoria": "Vestuário",
     "qtd": 3, "preco": 89.90},
]

RESTRIÇÕES:
- for obrigatório
- Calcular imposto dentro do loop
- Arredondar para 2 casas decimais
"""
# SUA SOLUÇÃO:


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
# SUA SOLUÇÃO:


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


# =============================================================================
# EXERCÍCIO 08 | Dicionários e métodos
# Nível: Médio | Contexto: Cardápio de restaurante
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
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
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 09 | Sets
# Nível: Médio | Contexto: Sistema de permissões
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de controle de acesso onde cada usuário
tem um conjunto de permissões.

TAREFA:
Crie as funções:

- tem_permissao(permissoes: set, acao: str) -> bool

- permissoes_faltando(permissoes_usuario: set,
                       permissoes_necessarias: set) -> set
  Retorna o que falta para o usuário ter acesso total

- permissoes_em_comum(grupo_a: set, grupo_b: set) -> set

- pode_acessar_modulo(permissoes: set,
                       modulo: str) -> dict
  Módulos e permissões necessárias:
  "financeiro"   → {"ver_financeiro", "editar_financeiro"}
  "rh"          → {"ver_rh"}
  "admin"       → {"admin", "super_admin"}
  Retorna {"acesso": True/False, "faltando": set()}

- unificar_equipe(equipes: list) -> set
  Recebe lista de sets e retorna todas as permissões únicas

RESTRIÇÕES:
- Operações de set obrigatórias: &, |, -, <=
- Sem converter para lista em nenhum momento
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 10 | Funções com argumentos variados
# Nível: Médio | Contexto: Gerador de relatórios
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de geração de relatórios flexível onde
os parâmetros variam conforme o tipo de relatório.

TAREFA:
Crie a função gerar_relatorio(titulo: str,
                               *dados,
                               separador: str = "-",
                               largura: int = 40,
                               **configuracoes) -> str que:
- Gere um relatório formatado como string
- *dados: linhas de conteúdo do relatório
- separador e largura: formatação do cabeçalho
- **configuracoes: metadados extras (autor, data, versao etc)

SAÍDA ESPERADA:
========================================
RELATÓRIO DE VENDAS
========================================
Total: R$ 15.000,00
Vendedor: Carlos
Meta atingida: True
----------------------------------------
Autor: Ana
Data: 2024-03-01
========================================

RESTRIÇÕES:
- *args e **kwargs obrigatórios
- f-strings para formatação
- Sem bibliotecas externas
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 11 | Classe básica
# Nível: Médio | Contexto: Sistema de produto
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
E-commerce precisa de uma classe para representar produtos.

TAREFA:
Crie a classe Produto com:
- __init__(self, codigo, nome, preco, estoque)
- aplicar_desconto(percentual: float) → altera o preço
- adicionar_estoque(qtd: int)
- remover_estoque(qtd: int) → raise ValueError se insuficiente
- esta_disponivel() -> bool
- valor_em_estoque() -> float  (preco * estoque)
- __str__() → representação legível
- __repr__() → representação técnica

RESTRIÇÕES:
- Validar preco e estoque no __init__ (não negativos)
- raise ValueError com mensagem clara
- @property para preco (não permite valor negativo via setter)
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 12 | Classe com métodos especiais
# Nível: Médio-Difícil | Contexto: Carrinho de compras
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de e-commerce precisa de um carrinho
que usa a classe Produto do exercício anterior.

TAREFA:
Crie a classe Carrinho com:
- __init__(self, cliente: str)
- adicionar(produto: Produto, quantidade: int)
  → não adiciona se sem estoque
- remover(codigo_produto: str) -> bool
- calcular_subtotal() -> float
- aplicar_cupom(desconto: float) → desconto no total
- finalizar() -> dict  → deduz estoque, retorna resumo
- __str__() → lista formatada dos itens
- __len__() → quantidade de itens diferentes

RESTRIÇÕES:
- Usar a classe Produto do Ex.11
- try/except em remover para produto não encontrado
- Não permitir finalizar carrinho vazio
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 13 | Encapsulamento
# Nível: Médio-Difícil | Contexto: Conta bancária
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema bancário com regras rígidas de acesso aos dados.

TAREFA:
Crie a classe ContaBancaria com encapsulamento real:
- __saldo privado (name mangling)
- __historico privado
- titular e agencia públicos
- @property saldo → só leitura
- depositar(valor) → valida valor positivo
- sacar(valor) → valida saldo suficiente
- transferir(valor, conta_destino: ContaBancaria)
- extrato() → imprime histórico formatado
- __str__() → resumo da conta

FORMATO DO HISTÓRICO:
[2024-03-01 08:22] DEPÓSITO    +R$1.500,00 | Saldo: R$1.500,00
[2024-03-01 08:23] SAQUE       -R$  200,00 | Saldo: R$1.300,00

RESTRIÇÕES:
- __saldo nunca acessível diretamente de fora
- datetime para timestamp
- raise ValueError com mensagem clara em operações inválidas
"""
# SUA SOLUÇÃO:


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


# =============================================================================
# EXERCÍCIO 15 | Combinação: listas + dicionários + funções
# Nível: Médio-Difícil | Contexto: Sistema de votação
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de votação para eleição interna de uma empresa.

TAREFA:
Crie as funções:

- registrar_voto(votos: dict, eleitor: str,
                  candidato: str,
                  eleitores_validos: set) -> dict
  → eleitor só pode votar uma vez
  → eleitor deve estar no set de válidos
  → retorna {"registrado": True/False, "mensagem": ...}

- apurar_resultado(votos: dict) -> dict
  → conta votos por candidato
  → retorna ordenado do mais votado

- verificar_vencedor(resultado: dict) -> str
  → retorna nome do vencedor
  → "SEGUNDO TURNO" se empate entre os dois primeiros

- relatorio_eleicao(votos: dict,
                     eleitores_validos: set) -> str
  → total de eleitores, votantes, abstenção (%)
  → resultado completo

RESTRIÇÕES:
- set para controlar quem já votou
- dicionário para contagem
- try/except em registrar_voto
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 16 | While + dicionário
# Nível: Médio | Contexto: Menu de sistema
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de gerenciamento de tarefas via terminal.

TAREFA:
Crie um sistema com menu interativo usando while que permita:
1 → Adicionar tarefa (nome, prioridade: alta/media/baixa)
2 → Listar tarefas ordenadas por prioridade
3 → Marcar tarefa como concluída
4 → Remover tarefas concluídas
5 → Estatísticas (total, concluídas, pendentes por prioridade)
0 → Sair

RESTRIÇÕES:
- while com break para sair
- Dados em lista de dicionários
- Validar todas as entradas do usuário
- try/except em todas as entradas numéricas
- Ordenação por prioridade: alta → media → baixa
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 17 | For + set + dicionário
# Nível: Médio | Contexto: Análise de acessos
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de análise de logs de acesso a um sistema.

TAREFA:
Dada a lista de logs, crie as funções:

- usuarios_unicos(logs: list) -> set
  → retorna set de usuários que acessaram

- acessos_por_usuario(logs: list) -> dict
  → conta quantos acessos cada usuário teve

- horario_pico(logs: list) -> str
  → retorna a hora com mais acessos (formato "HH")

- usuarios_suspeitos(logs: list,
                      limite: int = 5) -> set
  → usuários com mais de 'limite' acessos na mesma hora

ENTRADA:
logs = [
    {"usuario": "ana",    "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "carlos", "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "ana",    "horario": "08:23", "acao": "ACESSO"},
    {"usuario": "ana",    "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "bot_01", "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "bot_01", "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "bot_01", "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "bot_01", "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "bot_01", "horario": "08:22", "acao": "LOGIN"},
    {"usuario": "bot_01", "horario": "08:22", "acao": "LOGIN"},
]

RESTRIÇÕES:
- set obrigatório em usuarios_unicos e usuarios_suspeitos
- for em todas as funções
- Sem list comprehension (guarda para o próximo nível)
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 18 | Classe com @classmethod e @staticmethod
# Nível: Médio-Difícil | Contexto: Gerador de IDs
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema que gera e valida identificadores únicos
para transações financeiras.

TAREFA:
Crie a classe GeradorID com:
- Atributo de classe: contador = 0
- __init__(self, prefixo: str)
- gerar(self) -> str
  → formato: "PREFIXO-0001", "PREFIXO-0002"...
  → incrementa o contador de classe

- @classmethod total_gerados(cls) -> int
  → retorna quantos IDs foram gerados no total

- @classmethod resetar(cls)
  → zera o contador

- @staticmethod validar(id_str: str) -> bool
  → valida se o formato é correto (TEXTO-NUMERO)
  → retorna True/False

- @staticmethod extrair_prefixo(id_str: str) -> str
  → extrai o prefixo do ID

RESTRIÇÕES:
- @classmethod e @staticmethod obrigatórios
- Formatação do número com zfill(4)
- try/except em validar e extrair_prefixo
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 19 | Funções + listas + ordenação
# Nível: Médio-Difícil | Contexto: Ranking de vendas
# Status: [ ] Pendente | [ ] Enviado |[ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de ranking mensal de vendedores.

TAREFA:
Crie as funções:

- calcular_comissao(vendas: float, cargo: str) -> float
  Tabela de comissão:
  "Junior"  → 2% até R$10k, 3% acima
  "Pleno"   → 3% até R$15k, 5% acima
  "Senior"  → 5% até R$20k, 8% acima

- gerar_ranking(vendedores: list) -> list
  → ordena por total de vendas (decrescente)
  → adiciona posição, comissão e medalha:
    1º → "🥇", 2º → "🥈", 3º → "🥉", resto → ""

- resumo_ranking(ranking: list) -> str
  → retorna relatório formatado com top 3 destacado

ENTRADA:
vendedores = [
    {"nome": "Ana",    "cargo": "Senior", "vendas": 22000.0},
    {"nome": "Carlos", "cargo": "Pleno",  "vendas": 18000.0},
    {"nome": "Pedro",  "cargo": "Junior", "vendas": 9500.0},
    {"nome": "Julia",  "cargo": "Senior", "vendas": 31000.0},
    {"nome": "Marcos", "cargo": "Pleno",  "vendas": 12000.0},
]

RESTRIÇÕES:
- sorted() com key obrigatório
- for para adicionar posição e medalha
- Arredondar comissão para 2 casas
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 20 | Classe + herança básica
# Nível: Difícil | Contexto: Sistema de notificações
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema que envia notificações por diferentes canais.

TAREFA:
Crie a hierarquia de classes:

Notificacao (classe base):
- __init__(destinatario, mensagem, prioridade)
- validar() -> bool  (mensagem não vazia, destinatario válido)
- formatar() -> str  (deve ser sobrescrito nas filhas)
- enviar() -> dict   (chama validar e formatar)
- __str__()

EmailNotificacao(Notificacao):
- __init__(destinatario, mensagem, prioridade, assunto)
- formatar() → formato de e-mail com assunto e corpo

SMSNotificacao(Notificacao):
- __init__(destinatario, mensagem, prioridade)
- formatar() → máximo 160 caracteres, trunca se necessário
- validar() → também valida se destinatário tem 11 dígitos

PushNotificacao(Notificacao):
- __init__(destinatario, mensagem, prioridade, titulo)
- formatar() → título + mensagem curta (máximo 100 chars)

RESTRIÇÕES:
- super().__init__() obrigatório nas filhas
- formatar() sobrescrito em cada filha
- try/except em enviar()
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 21 | Integração total — sem classe
# Nível: Difícil | Contexto: Sistema de biblioteca
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de empréstimo de livros de uma biblioteca.

TAREFA:
Usando apenas funções e estruturas de dados, crie:

- cadastrar_livro(acervo: dict, isbn: str,
                   titulo: str, autor: str,
                   copias: int) -> bool

- emprestar(acervo: dict, emprestimos: dict,
             isbn: str, usuario: str) -> dict
  → usuário só pode ter 3 livros ao mesmo tempo
  → livro precisa ter cópia disponível

- devolver(acervo: dict, emprestimos: dict,
            isbn: str, usuario: str) -> dict

- livros_disponiveis(acervo: dict) -> list
  → lista de livros com pelo menos 1 cópia livre

- relatorio_usuario(emprestimos: dict,
                     usuario: str) -> dict
  → livros em mãos do usuário

- livros_mais_emprestados(historico: list) -> list
  → top 3 mais emprestados

RESTRIÇÕES:
- Sem classes
- set para controle de usuários com pendência
- try/except em emprestar e devolver
- Mínimo 6 funções
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 22 | Integração total — com classe
# Nível: Difícil | Contexto: Sistema de estoque com POO
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de estoque orientado a objetos para um almoxarifado.

TAREFA:
Crie as classes:

Produto:
- codigo, nome, quantidade, estoque_minimo, preco_unitario
- @property status → "CRÍTICO", "BAIXO" ou "OK"
- valor_total() → quantidade * preco_unitario
- __str__()

Estoque:
- produtos: dict (codigo → Produto)
- adicionar_produto(produto: Produto)
- entrada(codigo, quantidade) → registra entrada
- saida(codigo, quantidade) → impede se insuficiente
- produtos_criticos() -> list → status CRÍTICO ou BAIXO
- valor_total_estoque() -> float
- relatorio() -> str → relatório completo formatado
- __len__() → total de produtos cadastrados

MovimentacaoEstoque:
- historico de todas entradas e saídas
- registrar(tipo, codigo, quantidade, data)
- extrato(codigo: str) -> list → movimentações do produto

RESTRIÇÕES:
- @property obrigatório em Produto
- __len__ obrigatório em Estoque
- raise ValueError em saida() se insuficiente
- datetime para registrar data
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 23 | String + conversão + condicionais
# Nível: Médio | Contexto: Validador de documentos
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema que valida diferentes tipos de documentos
recebidos em vários formatos.

TAREFA:
Crie a função validar_documento(tipo: str,
                                  valor: str) -> dict que valide:

"cpf"    → 11 dígitos numéricos
"cnpj"   → 14 dígitos numéricos
"cep"    → 8 dígitos numéricos
"email"  → contém @ e . após o @
"placa"  → formato antigo AAA-9999 ou novo AAA9A99
           (sem verificar dígito verificador)
"telefone" → 10 ou 11 dígitos numéricos

Retorna:
{
    "tipo": ...,
    "valor_original": ...,
    "valor_limpo": ...,
    "valido": True/False,
    "motivo": "..." se inválido
}

RESTRIÇÕES:
- Sem biblioteca re (regex)
- isdigit(), isalpha(), isalnum() obrigatórios
- try/except no bloco principal
- Uma função por tipo de validação + função roteadora
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 24 | Loop + lista + dicionário + try/except
# Nível: Difícil | Contexto: Processador de pedidos
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema que processa uma fila de pedidos com
regras de negócio complexas.

TAREFA:
Crie a função processar_fila_pedidos(pedidos: list,
                                      estoque: dict) -> dict que:
- Processe cada pedido da fila em ordem
- Verifique disponibilidade no estoque
- Aprove se tiver estoque, rejeite se não tiver
- Atualize o estoque a cada aprovação
- Pedidos com valor acima de R$10.000 precisam de "aprovacao_manual"
- Retorne:
  {
    "aprovados": [...],
    "rejeitados": [...],
    "aprovacao_manual": [...],
    "estoque_final": {...},
    "total_faturado": 0.0
  }

ENTRADA:
pedidos = [
    {"id": 1, "produto": "Notebook",  "qtd": 2, "preco": 3500.00},
    {"id": 2, "produto": "Mouse",     "qtd": 50,"preco": 120.00},
    {"id": 3, "produto": "Monitor",   "qtd": 3, "preco": 1200.00},
    {"id": 4, "produto": "Invisivel", "qtd": 1, "preco": 100.00},
]
estoque = {"Notebook": 5, "Mouse": 30, "Monitor": 10}

RESTRIÇÕES:
- for obrigatório para processar a fila
- try/except para produto não encontrado no estoque
- while não usar (só for neste exercício)
"""
# SUA SOLUÇÃO:


# =============================================================================
# EXERCÍCIO 25 | PROJETO INTEGRADOR — tudo junto
# Nível: Difícil | Contexto: Mini sistema de vendas completo
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Este é o exercício mais importante dos 25.
Você vai construir um mini sistema de vendas completo
usando tudo que aprendeu até aqui.

TAREFA:
Construa um sistema com as seguintes classes e funções:

CLASSES:
- Produto(codigo, nome, preco, estoque)
- Cliente(cpf, nome, email, limite_credito)
- Pedido(cliente, lista de itens)
  → calcular_total()
  → aplicar_desconto(percentual)
  → finalizar() → deduz estoque, retorna resumo

FUNÇÕES DE CONTROLE:
- cadastrar_cliente(clientes: dict, dados: dict) -> dict
  → valida CPF (11 dígitos) e email (tem @ e ponto)

- registrar_pedido(pedidos: list,
                    clientes: dict,
                    estoque: dict,
                    cpf_cliente: str,
                    itens: list) -> dict
  → valida cliente, verifica estoque, cria pedido

- relatorio_vendas(pedidos: list) -> str
  → total faturado, ticket médio,
  → cliente que mais comprou, produto mais vendido

MENU INTERATIVO (while):
1 → Cadastrar cliente
2 → Registrar pedido
3 → Ver relatório
4 → Listar clientes
5 → Ver estoque
0 → Sair

RESTRIÇÕES:
- POO obrigatório para as 3 classes
- Funções separadas para cada operação
- try/except em todas as entradas do usuário
- set para controlar CPFs já cadastrados
- while com break para o menu
- Mínimo 10 funções/métodos no total
"""
# SUA SOLUÇÃO:


# =============================================================================
# VERIFICAÇÃO DE PROGRESSO
# =============================================================================
print("=" * 55)
print("25 EXERCÍCIOS — REVISÃO GERAL FASE 1")
print("=" * 55)
exercicios = [
    "01 - Tipos e conversão de dados",
    "02 - Fatiamento de strings",
    "03 - Estruturas condicionais (IR + bônus)",
    "04 - While com break (pagamento)",
    "05 - For com listas (nota fiscal)",
    "06 - Try/except múltiplos erros",
    "07 - Listas e métodos (fila)",
    "08 - Dicionários e métodos (cardápio)",
    "09 - Sets (permissões)",
    "10 - Funções *args e **kwargs",
    "11 - Classe Produto",
    "12 - Classe Carrinho",
    "13 - Encapsulamento (conta bancária)",
    "14 - Listas de objetos (RH)",
    "15 - Listas + dicionários + funções (votação)",
    "16 - While + dicionário (menu tarefas)",
    "17 - For + set + dicionário (logs)",
    "18 - @classmethod e @staticmethod",
    "19 - Funções + ordenação (ranking)",
    "20 - Herança (notificações)",
    "21 - Integração sem classe (biblioteca)",
    "22 - Integração com classe (estoque)",
    "23 - String + conversão (documentos)",
    "24 - Loop + pedidos + estoque",
    "25 - PROJETO INTEGRADOR COMPLETO",
]
for i, ex in enumerate(exercicios, 1):
    print(f"[ ] {ex}")
print("-" * 55)
print("Regra: Enviar para revisão antes de avançar")
print("Regra: Todo exercício commitado no GitHub")
print("=" * 55)
