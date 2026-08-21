'''12. Um usuário vai fazer uma longa viagem. Faça um programa que peça a capacidade do tanque
do carro (em litros), o consumo médio do carro (quantos quilômetros ele faz por litro) e o preço
atual do litro da gasolina. Calcule e exiba:
a. Qual a distância máxima que o carro consegue percorrer com o tanque cheio?
b. Quanto custará (em R$) para encher o tanque completamente vazio?'''
C, CM, G = map(int, input().split())
print (C*CM, G*C)