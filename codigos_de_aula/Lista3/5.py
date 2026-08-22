'''Cenário: No IFRN, as notas vão de 0 a 100. Vamos programar um sistema que calcula a
média aritmética simples de duas notas bimestrais e define o futuro acadêmico do estudante.
• A Condição: Leia a nota1 e a nota2 do aluno. Calcule a média e faça as seguintes
verificações:
o Se a média for maior ou igual a 60: "Parabéns, você foi APROVADO!"
o Se a média for menor que 60 E maior ou igual a 20: "Você ficou em RECUPERAÇÃO!
Estude para a prova final."
o Se a média for menor que 20: "REPROVADO direto."'''
Nota1, Nota2 = map(int, input().split())
if (Nota1+Nota2)/2 >=60:
	print("Parabéns, você foi APROVADO!")
elif 20<=(Nota1+Nota2)/2 <60:
	print("Você ficou em RECUPERAÇÃO! Estude para a prova final.")
else:
	print("REPROVADO direto.")