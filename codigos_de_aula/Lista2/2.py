'''2. Um caixa eletrônico precisa dispensar o dinheiro com a menor quantidade de notas possível.
Faça um programa que leia um valor inteiro em Reais (R$) que o usuário deseja sacar. O
programa deve calcular e exibir quantas notas de 100, 50, 20, 10, 5, 2 e 1 real serão entregues.'''
A = int(input())
B,C,D,E,F,G,H = 0,0,0,0,0,0,0
while A>=100:
    A-=100
    B+=1
while A>=50:
    A-=50
    C+=1
while A>=20:
    A-=20
    D+=1
while A>=10:
    A-=10
    E+=1
while A>=5:
    A-=5
    F+=1
while A>=2:
    A-=2
    G+=1
while A>=1:
    A-=1
    H+=1
print (f"{B} NOTAS DE 100\n {C} NOTAS DE 50 \n{D} NOTAS DE 20 \n{E} NOTAS DE 10 \n{F} NOTAS DE 5 \n{G} NOTAS DE 2 \n{H} NOTA DE 1")