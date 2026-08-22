'''Faça um programa onde o usuário informa o dia da semana atual usando um número (0 para
Domingo, 1 para Segunda, 2 para Terça... até 6 para Sábado). Em seguida, ele informa uma
quantidade de dias que irá aguardar para um evento. O programa deve calcular e exibir qual
será o dia da semana (em número de 0 a 6) após essa quantidade de dias.
Exemplo: Se hoje é 2 (Terça) e ele vai esperar 10 dias, o evento cairá no dia 5 (Sexta). Use o
operador módulo (%).'''
Dia_atual, dia_evento = map(int,input().split())
print((Dia_atual+dia_evento) %7)