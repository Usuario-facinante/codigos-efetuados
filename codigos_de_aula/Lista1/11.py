'''11. Você e seus amigos foram a uma pizzaria. Escreva um programa que solicite o valor total da
conta consumida e a quantidade de pessoas na mesa. O programa deve adicionar uma taxa de
serviço de 10% (gorjeta) sobre o valor total e, em seguida, calcular e exibir na tela quanto cada
amigo deve pagar dividindo a conta igualmente.'''
VL, Q = map(int, input().split())
VL = VL + (VL*(10/100))
print (VL/Q)