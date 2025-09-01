import random

numero_secreto = random.randint(1, 10)
tentativas = 0

print("🎯 Tente adivinhar o número entre 1 e 10!")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1

    if tentativa < 1 or tentativa > 10:
        print("⛔ Número fora do intervalo! Tente entre 1 e 10.")
        continue  # pula para a próxima tentativa sem contar como erro

    if tentativa == numero_secreto:
        print(f"✅ Parabéns, Patricia! Você acertou em {tentativas} tentativas.")
        break  # encerra o jogo
    elif tentativa < numero_secreto:
        print("🔼 Tente um número maior.")
    else:
        print("🔽 Tente um número menor.")
        
# random é um módulo, não uma função nem um método.
