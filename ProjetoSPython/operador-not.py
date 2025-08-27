# not (NÃO)
# Inverte o valor lógico. Se algo é True, vira False, e vice-versa.

# Simulação de login
usuario_logado = False

if not usuario_logado:
    print("Você precisa fazer login para continuar.")
else:
    print("Bem-vindo de volta!")
    
    
#- A variável usuario_logado está como False, ou seja, o usuário não está logado.
#- O not usuario_logado inverte isso para True, então a mensagem de login aparece.
#- Se usuario_logado fosse True, o not transformaria em False, e o programa mostraria "Bem-vindo de volta!"
