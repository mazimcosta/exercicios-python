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
