A, B = map(float, input().split())
if (A + B)/2 >= 7:
    print ("Aprovado")
elif 4 <= (A + B)/2 < 7:
    print ("Recuperação")
else:
    print("Reprovado")