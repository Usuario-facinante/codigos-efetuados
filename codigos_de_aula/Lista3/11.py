'''O Bug do Calendário Temporal no Servidor do IFRN
• Cenário: Você faz parte da equipe de TI do IFRN Campus Parnamirim e o servidor central
de matrículas apresentou uma falha lógica de sincronização. O sistema precisa registrar
quais turmas terão projetos especiais de pesquisa que só ocorrem no dia 29 de fevereiro!
Para corrigir esse problema, você precisa construir um script em Python que determine de
forma automática se um determinado ano fornecido pelo usuário é bissexto (ano com 366
dias) ou normal (ano com 365 dias).

Disciplina: Introdução à Programação
Professor: Givanaldo Rocha de Souza

• A Regra Lógica (Calendário Gregoriano): Para que um ano seja considerado bissexto, ele
deve atender a uma destas regras matemáticas:
1. Ele deve ser divisível por 4 E não ser divisível por 100.
2. OU ele deve ser divisível por 400.'''
Ano = int(input())
if Ano % 4 == 0 and Ano % 100 != 0:
	print ("Ano Bisexto.")
elif Ano % 400 == 0:
	print("Ano Bisexto.")
else:
	print("Ano normal.")