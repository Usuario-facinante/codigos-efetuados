'''Classificador de Maratonista de Séries e Animes
• Cenário: Chegou o fim de semana e você quer descobrir se o seu nível de maratona de
animes na Crunchyroll ou séries na Netflix está saudável.
• A Condição: Peça para o usuário digitar a quantidade de horas que ele passa assistindo a
telas por dia. O programa deve classificar o perfil usando if, elif e else:
o Menos de 1 hora: "Espectador Casual"
o De 1 a 3 horas: "Maratonista Iniciante"
o Mais de 3 horas até 5 horas: "Maratonista Profissional"
o Mais de 5 horas: "Alerta Vermelho! Desligue a tela e vá ver o sol!'''
Quantidade_de_horas = float(input())
if 1>Quantidade_de_horas:
	print("Espectador Casual")
elif 1<=Quantidade_de_horas<=3:
	print("Maratonista iniciante")
elif 3<Quantidade_de_horas<=5:
	print("Maratonista Profissional")
else:
	print("Alerta  Vermelho! Desligue a tela e vá ver o sol!")