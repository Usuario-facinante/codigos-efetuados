'''A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 etc. A regra de formação é
simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois
anteriores. Implemente um algoritmo que leia um número inteiro calcule o seu número de
Fibonacci. F1 = 1, F2 = 1, F3 = 2 etc.'''
Numero, lista = int(input("Digite um número inteiro para descobrir o número em forma Fibonacci.\n")), [1,1]
for _ in range (Numero):
    if Numero <=2:
        break
    Numero-=1
    lista.append(lista[_]+lista[_+1])
print(max(lista))