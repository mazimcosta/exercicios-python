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
# TESTES — FONTE "arquivo"
# =========================

("arquivo", "linha 1\nlinha 2\nlinha 3")

("arquivo", None)

("arquivo", 12345)


# =========================
# TESTES — FONTE "numero"
# =========================

("numero", "25")

("numero", "abc")

("numero", "-9")

("numero", None)


# =========================
# TESTES — FONTE "lista"
# =========================

("lista", [10, 20, 30])

("lista", [])

("lista", None)

("lista", "python")


# =============================
# TESTES — FONTE "dicionario"
# =============================

("dicionario", {"valor": 150})

("dicionario", {"preco": 100})

("dicionario", {})

("dicionario", None)


# =========================
# TODOS OS TESTES JUNTOS
# =========================

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
