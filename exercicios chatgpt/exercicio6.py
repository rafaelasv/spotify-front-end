
"""Exercício 6: Conversor de Temperatura 
Crie um programa que:  
1. Peça ao usuário uma temperatura em graus Celsius.  
2. Converta essa temperatura para Fahrenheit usando a fórmula:  
  
3. Mostre a mensagem:  
   - "[Celsius] graus Celsius equivalem a [Fahrenheit] graus Fahrenheit." """

celsius = int(input("Digite uma temperatura em graus Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.")