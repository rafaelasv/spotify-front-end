
"""Exercício 7: Calculadora de IMC**  
Crie um programa que:  
1. Peça ao usuário o peso (em kg) e a altura (em metros).  
2. Calcule o Índice de Massa Corporal (IMC) usando a fórmula:  
 IMC = (Peso/altura)2
3. Mostre a mensagem:  
   - "Seu IMC é [resultado]."  
4. Opcional: Adicione interpretações baseadas no valor do IMC:  
   - Menor que 18.5: Abaixo do peso.  
   - Entre 18.5 e 24.9: Peso normal.  
   - Entre 25 e 29.9: Sobrepeso.  
   - 30 ou mais: Obesidade.  """

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (em metros): "))  

imc = peso / (altura ** 2)  


print(f"Seu IMC é {imc:.2f}.")  # Formata o resultado para 2 casas decimais

# Adiciona interpretações automáticas
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está no peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
