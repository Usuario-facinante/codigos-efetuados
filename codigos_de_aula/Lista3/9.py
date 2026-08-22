'''Meia-Entrada ou Gratuidade no Trem
• Cenário: Você e seus colegas estão planejando um passeio de trem saindo da estação de
Parnamirim rumo a Natal e precisam calcular o preço da passagem.
• A Condição: O programa deve perguntar a idade do usuário e se ele possui carteira de
estudante ativa (o usuário deve responder com "sim" ou "não").
o Se a idade for igual ou superior a 60 anos, o transporte é gratuito: "Gratuidade
concedida por lei!"
o Se o usuário tiver menos de 18 anos OU possuir carteira de estudante ativa ("sim"),
ele tem direito a pagar metade: "Meia-entrada autorizada!"
o Senão, exiba: "Passagem inteira."'''
Idade_do_usuario = int(input("Qual a sua idade? "))
Carteira_de_estudante = int(input("Possui Carteira de estudante ativa? "))
if Idade_do_usuario >= 60:
	print("Gratuidade concedida por lei!")
elif Idade_do_usuario < 18 or Carteira_de_estudante.lower() == "Sim":
	print("Meia-entrada autorizada!")
else:
	print("Passagem inteira.")