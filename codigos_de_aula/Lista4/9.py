'''Dado um número inteiro positivo, determine a sua decomposição em fatores primos. Ex.: 630 = 2 x
3 x 3 x 5 x 7'''
Inteiro = int(input("Digite o numero inteiro para descobrir qual é a sua decomposição em fatores primos.\n"))
calc = []
if Inteiro >= 1:
    for _ in range (2, Inteiro):
        if Inteiro % _ == 0:
            while Inteiro % _ == 0:
                calc.append(_)
                Inteiro //= _
print (f"A decomposição em fatores primos do numero dado é: {" x ".join(map(str, calc))}")