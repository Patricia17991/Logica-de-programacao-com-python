# Calculadora simples
#DESAFIO 2
#OBS! nesta o resultado está sendo retornado como ponto flutuante (ex: 10.0), mude o código para que retorne como número inteiro (ex:10).

# Solicita os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza o cálculo com base na operação
if operacao == "+":
    resultado = num1 + num2
    mensagem = f"A soma de {num1} e {num2} é {resultado}"
elif operacao == "-":
    resultado = num1 - num2
    mensagem = f"A subtração de {num1} por {num2} é {resultado}"
elif operacao == "*":
    resultado = num1 * num2
    mensagem = f"A multiplicação de {num1} por {num2} é {resultado}"
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        mensagem = f"A divisão de {num1} por {num2} é {resultado}"
    else:
        mensagem = "Erro: não é possível dividir por zero."
else:
    mensagem = "Operação inválida. Use apenas +, -, * ou /."

# Exibe o resultado
print("\n📢 Resultado:")
print(mensagem)

