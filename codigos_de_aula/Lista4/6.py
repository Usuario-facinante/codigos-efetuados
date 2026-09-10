"""Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar
se n é triangular."""
Numero = int(input("Digite um número para conferir se é triângular.\n"))
lista, result = [1, 2, 3], 0
while result<=Numero:
    result = lista[0] * lista[1] * lista[2]
    if result == Numero:
        print("O valor digitado é triângular.")
        break
    else:
        lista.append(lista[2]+1)
        lista.pop(2)
if result>Numero:
    print("Não é triângular.")