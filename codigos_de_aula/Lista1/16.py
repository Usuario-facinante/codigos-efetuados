'''16. O valor de uma corrida em um aplicativo de transporte é composto por uma taxa fixa inicial
(chamada de taxa de embarque) de R$ 4,00, mais R$ 1,50 por quilômetro rodado e R$ 0,25 por
minuto de viagem. Escreva um programa que pergunte a distância da viagem (em km) e a
duração (em minutos), calculando e exibindo o valor total que o passageiro deverá pagar.'''
D, T = map(float, input().split())
print (4.00+(1.50+D)+(0.15*T))