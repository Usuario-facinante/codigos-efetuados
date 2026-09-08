Numero = int(input("Digite um número para saber se ele é primo ou não."))
if Numero <= 1:
    print ("Não é primo")
else:
    div = 0
    for _ in range (2, Numero):
        if Numero % _ == 0:
            div +=1
            break
if div == 0:
    print(f"O número {Numero} é primo.")
else:
    print (f"O número {Numero} não é primo.")