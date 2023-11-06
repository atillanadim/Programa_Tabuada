#Algoritmo para uma tabudada
#entrar o primeiro numero para multiplicar
#entrar o segundo Numero para processar 
#fazer calculo
#imprimir na tela 
print("Programa Tabuada 2 ao 10")
primeiro_numero= input("Digite qualquer tecla para iniciar ")
for primeiro_numero in range(2,11):
  print("****Tabuada do",primeiro_numero,("****"))
  for segundo_numero in range (11):
    print("{} x {} = {}".format(primeiro_numero,segundo_numero,
                              primeiro_numero*segundo_numero))
  
  
  


