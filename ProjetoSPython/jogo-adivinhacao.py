import random

# Gera um número secreto entre 1 e 10
numero_secreto = random.randint(1, 10)

print("🎲 Jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")
print("Digite 0 para desistir.\n")

while True:  # Simula um do...while: executa pelo menos uma vez
    tentativa = int(input("Seu palpite: "))

    if tentativa == 0:
        print("Você desistiu. O número era", numero_secreto)
        break
    elif tentativa == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    else:
        print("❌ Errado! Tente novamente.\n")
        
        

# while True garante que o loop rode pelo menos uma vez — como um do...while.
# break interrompe o loop quando o usuário acerta ou desiste.
# elif e else ajudam a tratar os diferentes cenários.
# Objetivo do código: O usuário precisa adivinhar um número secreto entre 1 e 10. O programa continua pedindo até acertar ou digitar "0" para desistir.
