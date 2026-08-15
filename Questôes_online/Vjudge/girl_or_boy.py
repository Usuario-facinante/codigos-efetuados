"""Naquela época, muitos meninos usavam fotos de meninas bonitas como avatares em fóruns. Então, é bem difícil saber o gênero de um usuário à primeira vista. No ano passado, nosso herói foi a um fórum e teve uma boa conversa com uma beleza (ele achou que sim). Depois disso, eles conversaram muito e, eventualmente, se tornaram um casal na rede.

Mas ontem, ele veio ver "ela" no mundo real e descobriu que "ela" é, na verdade, um homem muito forte! Nosso herói está muito triste e cansado demais para amar de novo agora. Então ele criou uma forma de reconhecer o gênero dos usuários pelos nomes de usuário.

Esse é o método dele: se o número de caracteres distintos no nome de usuário de alguém for ímpar, então ele é homem, caso contrário ela é mulher. Você recebe a string que indica o nome do usuário, por favor, ajude nosso herói a determinar o gênero desse usuário pelo método dele."""


A = input()
if len(set(A)) % 2 == 0:
	print ("CHAT WITH HER!")
else:
	print ("IGNORE HIM!")