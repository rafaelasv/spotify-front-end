"""Desafio: Média dos Números
Crie uma lista com pelo menos 5 números.
Calcule a soma dos números da lista.
Encontre a média (divida a soma pelo número de elementos na lista).
Mostre o resultado da soma e da média.
Dica: Use a função len(lista) para descobrir quantos elementos há na lista."""

numeros = [1, 2, 3, 4, 5]

soma= sum(numeros)
print(f"O resultado da soma eh {soma}.")

elementos = len(numeros)
print(f"Ha {elementos} elementos na lista.")

media = soma / elementos
print(f"A media dos numeros da lista e dos elementos dela eh {media:.2f}")