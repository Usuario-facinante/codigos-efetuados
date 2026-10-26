contagem = int(input())
lista = list(map(int, input().split()))
menor = abs(lista[1] - lista[0])
for a in range (contagem -1):
    distancia = abs(lista[a-1] - lista[a])
    if menor > distancia:
        menor = distancia
print (menor)