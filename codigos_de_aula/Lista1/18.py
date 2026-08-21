'''18. Faça um programa que peça o tamanho de um arquivo que o usuário deseja baixar (em MB) e a
velocidade do seu link de Internet (em Mbps - Megabits por segundo). Calcule e informe o tempo
aproximado de download do arquivo em minutos.'''
T, V = map(float, input().split())
T*=1000000
print ((T*V)/60)