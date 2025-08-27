#Uso do AND, OR, NOT
# Informações do usuário
idade = 20
é_estudante = True

# Verificações usando and, or, not
if idade >= 18 and é_estudante:
    print("Você é maior de idade e estudante.")

if idade < 18 or not é_estudante:
    print("Você é menor de idade ou não é estudante.")

if not (idade < 18):
    print("Você não é menor de idade.")
    
    