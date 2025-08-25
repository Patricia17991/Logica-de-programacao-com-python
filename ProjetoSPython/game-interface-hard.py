#🧠 Modo Difícil
# O número secreto vai de 1 a 500.
# Você tem apenas 5 tentativas.
# As dicas são mais vagas (sem dizer se é maior ou menor).

#⚡ Modo Relâmpago
# Você tem 15 segundos para acertar.
# O tempo é contado com um cronômetro.
# Se o tempo acabar, o jogo termina automaticamente.

import tkinter as tk
import random
import threading
import time

# Variáveis globais
numero_secreto = 0
tentativas = 0
pontuacao = 100
limite = 0
modo = ""
tempo_restante = 15
cronometro_ativo = False

# Função para iniciar o jogo
def iniciar_jogo(modo_selecionado):
    global numero_secreto, tentativas, pontuacao, limite, modo, tempo_restante, cronometro_ativo
    modo = modo_selecionado
    tentativas = 0
    pontuacao = 100
    tempo_restante = 15
    cronometro_ativo = False
    entry["state"] = "normal"
    botao_enviar["state"] = "normal"
    resultado["text"] = ""

    if modo == "difícil":
        numero_secreto = random.randint(1, 500)
        limite = 5
        info["text"] = "Modo Difícil: Adivinhe entre 1 e 500. 5 tentativas."
    elif modo == "relâmpago":
        numero_secreto = random.randint(1, 100)
        limite = 999  # ilimitado, mas com tempo
        info["text"] = "Modo Relâmpago: Adivinhe entre 1 e 100. Tempo: 15s."
        cronometro_ativo = True
        threading.Thread(target=cronometro).start()

# Função do cronômetro
def cronometro():
    global tempo_restante
    while tempo_restante > 0:
        time.sleep(1)
        tempo_restante -= 1
        info["text"] = f"⏱️ Tempo restante: {tempo_restante}s"
    resultado["text"] = f"⏰ Tempo esgotado! O número era {numero_secreto}."
    entry["state"] = "disabled"
    botao_enviar["state"] = "disabled"

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
        entry["state"] = "disabled"
        botao_enviar["state"] = "disabled"
        return

    tentativas += 1
    pontuacao -= 10

    if palpite == numero_secreto:
        resultado["text"] = f"🎉 Acertou! Tentativas: {tentativas}, Pontuação: {pontuacao}"
        entry["state"] = "disabled"
        botao_enviar["state"] = "disabled"
    elif modo == "difícil":
        resultado["text"] = "❓ Errado! Tente novamente."
        if tentativas >= limite:
            resultado["text"] = f"😢 Fim de jogo! Número era {numero_secreto}."
            entry["state"] = "disabled"
            botao_enviar["state"] = "disabled"
    else:
        if palpite < numero_secreto:
            resultado["text"] = "🔼 Tente um número maior."
        else:
            resultado["text"] = "🔽 Tente um número menor."

    entry.delete(0, tk.END)

# Interface gráfica
janela = tk.Tk()
janela.title("Jogo de Adivinhação Avançado")

tk.Label(janela, text="Escolha o modo de jogo:").pack()

tk.Button(janela, text="Modo Difícil", command=lambda: iniciar_jogo("difícil")).pack()
tk.Button(janela, text="Modo Relâmpago", command=lambda: iniciar_jogo("relâmpago")).pack()

info = tk.Label(janela, text="")
info.pack()

entry = tk.Entry(janela, state="disabled")
entry.pack()

botao_enviar = tk.Button(janela, text="Enviar Palpite", command=verificar_palpite, state="disabled")
botao_enviar.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()

# Dicas para turbinar ainda mais:
# Adicionar sons de acerto/erro com pygame.
# Criar ranking com nomes e pontuação.
# Salvar histórico em arquivo .txt ou .json.
