'''Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.'''
lista, Positivo, Media = [], 0, 0
for a in range (6):
    Numero = float(input())
    lista.append(Numero)
for _ in range (len(lista)):
    if lista[_] > 0:
        Positivo += 1
        Media += lista[_]
print (f"{Positivo} valores positivos\n{Media/Positivo:.1f}")
