#Questão 2 - App de Açaí 

#Mensagem de bem-vindo ao app 
print("Bem-vindo à Loja de Açaí e Cupuaçu da Rafaela Tavares!") 

#Descrição do cardápio com os tamanhos e preços
print("\nConfira nosso cardápio:") 

print("\nTemos 3 opções de tamanhos para você selecionar quantos adicionais quiser!") 
print("--------------------------------------------------")
print("                  Cardápio                        ")
print("--------------------------------------------------")
print("---| Tamanho  | Cupuaçu (CP) | Açaí (AC) |---")
print("---|    P     |   R$ 9.00    |  R$ 11.00 |---")
print("---|    M     |   R$ 14.00   |  R$ 16.00 |---")
print("---|    G     |   R$ 18.00   |  R$ 20.00 |---")
print("--------------------------------------------------")

#Cria o grupo com as possibilidades da escolha
precos = {
    "CP": {"P": 9, "M": 14, "G": 18},
    "AC": {"P": 11, "M": 16, "G": 20}
}

total_pedido = 0  # Acumulador para somar o valor total dos pedidos

while True:
    #Pede o sabor desejado e valida a entrada
    sabor = input("\nDigite o sabor desejado (CP para Cupuaçu ou AC para Açaí): ").upper()
    if sabor not in precos:
        print("Sabor inválido. Tente novamente.")
        continue  # Volta ao início do loop

    #Pede o sabor desejado e valida a entrada
    tamanho = input("Digite o tamanho desejado (P, M ou G): ").upper()
    if tamanho not in precos[sabor]:
        print("Tamanho inválido. Tente novamente.")
        continue  # Volta ao início do loop

    # Calcula o preço do item escolhido
    preco = precos[sabor][tamanho]
    total_pedido += preco  # Adiciona ao total acumulado

    print(f"Você pediu um {sabor} tamanho {tamanho}, no valor de R$ {preco:.2f}.")
    
    # Pergunta se o usuário deseja pedir mais alguma coisa
    continuar = input("Deseja pedir mais alguma coisa? (S para Sim, N para Não): ").upper()
    if continuar == "N":
        break  # Encerra o loop

# Exibe o valor total do pedido
print(f"\nTotal do seu pedido: R$ {total_pedido:.2f}")
print("Obrigado por comprar conosco!")