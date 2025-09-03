import random

numero_secreto = random.randint(1, 10)
tentativas = 0 #A contagem precisa começar de algum ponto, o ideal é que ela parta do zero, por isso o zero aqui
#se a contagem não tiver um começo ela não existe, é uma questão de lógica


print("🎯 Tente adivinhar o número entre 1 e 10!")

while True:#enquanto o número não for encontrado continue a executar
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1 #adicione +1 

    if tentativa < 1 or tentativa > 10:
        print("⛔ Número fora do intervalo! Tente entre 1 e 10.")
        continue  # pula para a próxima tentativa sem contar como erro

    if tentativa == numero_secreto:
        print(f"✅ Parabéns, Patricia! Você acertou em {tentativas} tentativas.")
        break  # encerra o jogo quando o número sorteado é encontrado
    elif tentativa < numero_secreto:
        print("🔼 Tente um número maior.")# quando o número não foi achado ainda
    else:
        print("🔽 Tente um número menor.")#quando o número ainda não foi achado
        
# random é um módulo, não uma função nem um método.
# Vai executar um loop e encerrar ele depois do usuário tentar acertar o número 5 vezes.
