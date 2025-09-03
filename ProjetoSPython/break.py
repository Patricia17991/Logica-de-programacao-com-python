#BREAK - o "PARE AGORA" da programação
#Imagine que vc está procurando as suas chaves em vários bolsos.

bolsos = ["calça","jaqueta","mochila", "estojo"]

for bolso in bolsos:
   printf(f"Procurando no bolso: {bolso}")
   
   if bolso == "jaqueta":
      print("Achei minhas chaves!")
      break #PARE de procurar
   print("Não encontrei aqui...")
   
print("Hora de sair!")

#Resumindo - quando encontrar PARE de procurar