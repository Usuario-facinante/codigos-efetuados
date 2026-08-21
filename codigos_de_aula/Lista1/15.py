'''15. Você decidiu pintar a parede do seu quarto. Faça um programa que solicite a largura e a altura
da parede (em metros). Sabendo que 1 litro de tinta é suficiente para pintar 3 metros quadrados,
calcule e exiba:
a. A área total da parede.
b. A quantidade de litros de tinta necessários para realizar o trabalho.'''
L, A = map(int, input().split())
print (L*A, (L*A)//3)