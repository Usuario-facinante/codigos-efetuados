'''10. Você tem duas variáveis, A e B, que recebem dois valores inteiros digitados pelo usuário. Faça
um programa que troque os valores entre elas, ou seja, A passa a valer o valor de B e B passa a
valer o valor original de A. Imprima os valores na tela antes e depois da troca.
Regra para dificultar: Em Python, existe um truque rápido (A, B = B, A), mas vocês não podem
usar. Vocês também não podem criar uma terceira variável temporária. A troca deve ser feita
usando apenas operações matemáticas de adição (+) e subtração (-).'''
A, B = map(int,input().split())
print(A+B-A, B+A-B)