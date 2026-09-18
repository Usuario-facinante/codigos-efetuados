bandejas = int(input())
copos_derrubados = 0
for _ in range (bandejas):
    latas, copos = map(int, input().split())
    if latas > copos:
        copos_derrubados += copos
print(copos_derrubados)