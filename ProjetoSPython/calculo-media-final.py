# Solicita as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

print(f"\nMédia final: {media:.2f}")

# Avaliação do desempenho
if media >= 9.0:
    print("Desempenho: Excelente! 🏆")
elif media >= 7.0:
    print("Desempenho: Bom! 👍")
elif media >= 5.0:
    print("Desempenho: Regular. 😐")
else:
    print("Desempenho: Insuficiente. 😞")

# Decisão sobre aprovação
if media >= 7.0:
    print("Situação: Aprovado! 🎉")
elif media >= 5.0:
    print("Situação: Em recuperação. 📚")
else:
    print("Situação: Reprovado. 😔")