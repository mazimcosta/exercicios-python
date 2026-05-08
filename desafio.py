"""
CONTEXTO:
Você está criando um sistema simples para controlar o estoque de uma loja.

DADOS INICIAIS:

estoque = {
    "arroz": {"quantidade": 10, "preco": 5.0},
    "feijao": {"quantidade": 5, "preco": 8.0},
    "macarrao": {"quantidade": 8, "preco": 3.5}
}

TAREFA:

Crie funções para:

1. adicionar_produto(nome, quantidade, preco)
   - Se produto já existir → erro
   - Se quantidade/preço inválidos → erro
   - Adiciona no estoque

2. vender_produto(nome, quantidade)
   - Se produto não existir → erro
   - Se quantidade maior que estoque → erro
   - Subtrai do estoque
   - Retorna valor total da venda

3. listar_estoque()
   - Mostra todos produtos com:
     nome, quantidade e preço

4. valor_total_estoque()
   - Retorna o valor total do estoque (quantidade * preço)

REGRAS:

- Usar dicionário
- Criar funções separadas
- Validar TODOS os dados
- Usar try/except onde fizer sentido
- Retornar dicionário padrão:

{
    "sucesso": True/False,
    "mensagem": "...",
    "dados": ...
}

EXTRA (NÍVEL ACIMA):

- Criar menu interativo (while)
- Salvar e carregar estoque em JSON
"""