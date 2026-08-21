'''17. Uma receita clássica de bolo de cenoura leva 3 ovos, 2 xícaras de farinha e 1.5 xícaras de açúcar
para servir exatamente 4 pessoas. Crie um programa que pergunte ao usuário para quantas
pessoas ele deseja fazer o bolo. O programa deve calcular e exibir a nova quantidade necessária
de ovos, farinha e açúcar, mantendo a proporção matemática.'''
P = int(input())
if P>=1:
    print (f"{3*P} ovos\n{2*P} xícaras de farinha\n {1.5*P} de açúcar")