"""Exercício 5: Tabuada de Multiplicação
Crie um programa que:

Peça ao usuário um número inteiro.
Mostre a tabuada de multiplicação desse número, de 1 a 10.
Exemplo de saída para o número 5:

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
Dica: Use um loop for para gerar os números de 1 a 10."""


numero = int(input("Digite um número inteiro: "))

# Gera a tabuada de 1 a 10 para o número fornecido
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
