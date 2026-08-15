N = int (input())
n = []
for a in range (N):
    lista = []
    for x in range (N):
        formula = min(a,x, N-1-a, N-1-x)+1
        lista.append(formula)
    n.append(lista)
for lista in n:
    print (*lista)