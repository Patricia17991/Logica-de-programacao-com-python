#DESAFIO 1
# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza os cálculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Indefinida (divisão por zero)"
divisao_inteira = num1 // num2 if num2 != 0 else "Indefinida"
resto = num1 % num2 if num2 != 0 else "Indefinido"
exponenciacao = num1 ** num2

# Exibe os resultados
print("\nResultados dos cálculos:")
print(f"{num1} + {num2} = {soma}")
print(f"{num1} - {num2} = {subtracao}")
print(f"{num1} * {num2} = {multiplicacao}")
print(f"{num1} / {num2} = {divisao}")
print(f"{num1} // {num2} = {divisao_inteira}")
print(f"{num1} % {num2} = {resto}")
print(f"{num1} ** {num2} = {exponenciacao}")
#esse código já trata o caso de divisão por zero, que é um erro comum. 
