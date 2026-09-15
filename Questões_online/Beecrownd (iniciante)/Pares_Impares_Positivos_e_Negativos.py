'''Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.'''
Par, Impar, Positivo, Negativo = 0, 0, 0, 0
for a in range (5):
    Numero = int(input())
    if Numero % 2 == 0:
        Par += 1
    else:
        Impar += 1
    if Numero > 0:
        Positivo += 1
    if Numero < 0:
        Negativo += 1
print (f"{Par} valor(es) par(es)\n{Impar} valor(es) impar(es)\n{Positivo} valor(es) positivo(s)\n{Negativo} valor(es) negativo(s)")