count = int(input())
lista = list(map(int, input().split()))
lampada1, lampada2 = 0, 0
for a in range (count):
    if lista[a] == 1:
        if lampada1 == 0:
            lampada1 +=1
        else:
            lampada1 = 0
    if lista[a] == 2:
        if (lampada1 == 1 and lampada2 == 0) or (lampada1 == 0 and lampada2 == 1):
            lampada1, lampada2 = lampada2, lampada1
        elif lampada1 == 0 and lampada2 == 0:
            lampada2, lampada1 = 1, 1
        else:
            lampada1, lampada2 = 0, 0
print (f"{lampada1}\n{lampada2}")