import random

# Gera o número secreto
numero_secreto = random.randint(1, 100)
tentativas = 0
pontuacao = 100
limite = 7

print("🎮 Bem-vinda ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")
print(f"Você tem {limite} tentativas. Digite 0 para desistir.\n")

while tentativas < limite:
    palpite = int(input(f"Tentativa {tentativas + 1}: "))
    
    if palpite == 0:
        print(f"Você desistiu! O número era {numero_secreto}.")
        break

    tentativas += 1
    pontuacao -= 10

    if palpite == numero_secreto:
        print(f"🎉 Parabéns, Patricia! Você acertou em {tentativas} tentativa(s).")
        print(f"Pontuação final: {pontuacao}")
        break
    elif palpite < numero_secreto:
        print("🔼 Dica: Tente um número maior.\n")
    else:
        print("🔽 Dica: Tente um número menor.\n")

else:
    print(f"😢 Fim de jogo! Você usou todas as {limite} tentativas.")
    print(f"O número secreto era {numero_secreto}. Pontuação final: {pontuacao}")
    
#✨ O que esse código traz de novo:
# O número secreto agora vai de 1 a 100.
# Você tem 7 tentativas para acertar.
# Cada erro tira 10 pontos da pontuação inicial (100).
# O jogo dá dicas se o número é maior ou menor.
# E claro, você pode desistir a qualquer momento com 0.
