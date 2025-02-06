"""Exercício 1: Lista de Compras
Crie uma lista chamada compras com pelo menos 5 itens (ex.: arroz, feijão, pão).
Mostre todos os itens da lista um por um.
Adicione mais um item à lista.
Remova um item específico da lista."""

compras = ["arroz", "pão", "macarrão", "suco", "salgadinho"]

# Mostra todos os itens usando um loop
print("Lista de compras:")
for item in compras:
    print(item)

# Adiciona um item à lista
compras.append("chocolate")
print("\nApós adicionar chocolate:")
print(compras)

# Remove um item específico
compras.remove("suco")
print("\nApós remover suco:")
print(compras)
