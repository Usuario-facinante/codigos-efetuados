'''O Radar Eletrônico da Avenida Maria Lacerda
• Cenário: A prefeitura de Parnamirim instalou um radar inteligente na Avenida Maria Lacerda,
onde o limite máximo de velocidade é de 60 km/h.
• A Condição: Escreva um programa que leia a velocidade registrada de um veículo em km/h:
o Se a velocidade for menor ou igual a 60 km/h: "Velocidade permitida. Boa viagem!"
o Se a velocidade for maior que 60 km/h E menor ou igual a 70 km/h: "Infração Média!
Multa de R$ 130,16."
o Se a velocidade for maior que 70 km/h: "Infração Gravíssima! Multa de R$ 293,47 e
perda de pontos na CNH."'''
Velocidade = int(input())
if Velocidade <= 60:
	print("Velocidade permitida. Boa viagem!")
elif Velocidade>60 and Velocidade<=70:
	print("Infração média! Multa de R$ 130,16.")
else:
	print("Infração Gravíssima! Multa de R$ 293,47 e perda de pontos na CNH.")