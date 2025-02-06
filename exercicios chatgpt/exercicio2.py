"""Exercício 2: Soma Simples
Crie um programa que:

Peça ao usuário dois números.
Some esses dois números.
Mostre o resultado na tela, como:
"A soma de [número1] e [número2] é [resultado]."
Dica: Use input() para coletar os números e lembre-se de convertê-los para o tipo int ou float."""

numero1 = float(input("Digite um número: "))  # Converte a entrada para número decimal
numero2 = float(input("Digite outro número: "))  # Converte a entrada para número decimal
soma = numero1 + numero2  # Soma os dois números
print(f"A soma de {numero1} e {numero2} é {soma}.")  # Mostra o resultado

