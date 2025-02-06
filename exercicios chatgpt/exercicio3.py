"""Exercício 3: Calculadora de Média
Crie um programa que:

Peça três notas ao usuário.
Calcule a média das três notas.
Mostre a mensagem:
"As notas são: [nota1], [nota2], [nota3]. A média é [média]."
Dica: Use a fórmula da média:

Media = nota1 + nota2 + nota3 / 3"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a outra nota: "))
nota3 = float(input("Digite a outra nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"As notas são: {nota1}, {nota2}, {nota3}. A média é {media}.")


 
