'''10. Juiz de Par ou Ímpar Lógico
• Cenário: Dois amigos querem decidir quem joga primeiro no videogame clássico do
laboratório de redes, mas resolveram usar o Python como juiz imparcial.
• A Condição: O programa deve solicitar que o Jogador 1 escolha entre "par" ou "impar". Em
seguida, o Jogador 1 digita o seu número e o Jogador 2 digita o dele. O programa deve
somar os dois números.
o Se a escolha do Jogador 1 for "par" E a soma dos dois números for par (ou seja, soma
% 2 == 0), exiba: "Jogador 1 venceu!"
o elif a escolha do Jogador 1 for "impar" E a soma for ímpar (soma % 2 != 0), exiba:
"Jogador 1 venceu!"
o Senão, exiba: "Jogador 2 venceu!"'''
Jogador_1 = input()
Numero_1 = int(input())
Jogador_2 = input()
Numero_2 = int(input())
if Jogador_1.lower() == "par" and (Numero_1 + Numero_2) % 2 == 0:
	print("Jogador 1 venceu!")
elif Jogador_1.lower() == "impar" and (Numero_1 + Numero_2) % 2 != 0:
	print("Jogador 1 venceu!")
else:
	print("Jogador 2 venceu!")