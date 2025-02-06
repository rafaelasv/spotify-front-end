
"""Exercício 4: Verificador de Par ou Ímpar
Crie um programa que:

Peça ao usuário para digitar um número inteiro.
Verifique se o número é par ou ímpar.
Mostre a mensagem:
"O número [número] é par."
ou
"O número [número] é ímpar."
Dica: Use o operador de módulo (%) para verificar o resto da divisão por 2."""

numero = int(input("Digite um número inteiro: "))  # Entrada do número

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
