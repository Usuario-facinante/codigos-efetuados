'''1. Faça um programa que leia um valor inteiro representando uma quantidade de segundos.
Calcule e exiba a quantos dias, horas, minutos e segundos esse valor corresponde.
Dica: Lembre-se de usar a divisão inteira (//) e o operador de resto (%).'''
S, M, H, D = int(input()), 0, 0, 0
while S>=60:
    S-=60
    M+=1
while M>=60:
    M-=60
    H+=1
while H>=24:
    H-=24
    D+=1
print (f"SEGUNDOS = {S} MINUTOS = {M} HORAS = {H} DIAS = {D}")