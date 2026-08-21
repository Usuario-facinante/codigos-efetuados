'''20. Faça um programa que solicite o primeiro nome do usuário e depois o seu sobrenome. O
programa deve gerar e exibir uma sugestão de login (nome de usuário) juntando o nome, o
sobrenome e o número total de caracteres que compõem o nome completo.
Exemplo: se o usuário digitar "Ana" e "Silva", o login sugerido será "AnaSilva8", pois há 8 letras
no total.'''
N, SM = input().split()
A = len(N+SM)
A = str(A)
print (N+SM+A)