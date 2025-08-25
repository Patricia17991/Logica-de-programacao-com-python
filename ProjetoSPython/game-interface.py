import tkinter as tk #baixar lib
import random

# Número secreto e variáveis
numero_secreto = random.randint(1, 100)
tentativas = 0
pontuacao = 100
limite = 7

# Função de verificação
def verificar_palpite():
    global tentativas, pontuacao

    try:
        palpite = int(entry.get())
    except ValueError:
        resultado["text"] = "Digite um número válido!"
        return

    if palpite == 0:
        resultado["text"] = f"Você desistiu! O número era {numero_secreto}."
        botao["state"] = "disabled"
        return

    tentativas += 1
    pontuacao -= 10

    if palpite == numero_secreto:
        resultado["text"] = f"🎉 Acertou! Tentativas: {tentativas}, Pontuação: {pontuacao}"
        botao["state"] = "disabled"
    elif tentativas >= limite:
        resultado["text"] = f"😢 Fim de jogo! Número era {numero_secreto}. Pontuação: {pontuacao}"
        botao["state"] = "disabled"
    elif palpite < numero_secreto:
        resultado["text"] = "🔼 Tente um número maior."
    else:
        resultado["text"] = "🔽 Tente um número menor."

    entry.delete(0, tk.END)

# Interface gráfica
janela = tk.Tk()
janela.title("Jogo de Adivinhação")

tk.Label(janela, text="Adivinhe o número entre 1 e 100").pack()
entry = tk.Entry(janela)
entry.pack()

botao = tk.Button(janela, text="Enviar Palpite", command=verificar_palpite)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()