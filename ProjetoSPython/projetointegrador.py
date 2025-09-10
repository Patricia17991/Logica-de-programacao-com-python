numeros = []

# Laço 'while' para coletar a entrada do usuário
while True:
    entrada = input("Digite um número (ou 'sair' para terminar): ")
    
    # Condição de parada do laço 'while'
    if entrada.lower() == 'sair':
        break
    
    try:
        # Tenta converter a entrada para um número inteiro
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        # Se a entrada não for um número válido, exibe uma mensagem de erro
        print("Entrada inválida. Por favor, digite um número.")

  if numero:
        soma = 0
    
    # Laço 'for' para somar todos os números na lista
    for num in numeros:
        soma += num
        
    # Calcula a média
    media = soma / len(numeros)
    
    # Exibe os resultados
    print("\n--- Resultados ---")
    print(f"Você inseriu os seguintes números: {numeros}")
    print(f"A soma total é: {soma}")
    print(f"A média é: {media:.2f}") # O .2f formata a média com duas casas decimais
else:
    print("\nNenhum número foi inserido.")
    
