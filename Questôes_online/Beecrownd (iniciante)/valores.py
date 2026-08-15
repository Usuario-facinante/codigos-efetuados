'''Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada'''
x = []
for f in range (6):
    s = None
    s = float(input())
    if s >=0:
        x.append(s)
print (f"{len(x)} valores positivos")