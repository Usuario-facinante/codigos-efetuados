'''12. Mutirão de Pintura no Grêmio Estudantil do IFRN
• Cenário: O Grêmio Estudantil do IFRN Campus Parnamirim vai passar por uma reforma e
os alunos decidiram fazer um mutirão para pintar as paredes da nova sala de convivência.
Como estudante do curso Técnico em Informática, você se voluntariou para criar um
programa em Python que ajude a equipe a calcular a quantidade exata de latas de tinta
necessárias e o custo total do projeto, evitando desperdícios.
• As Regras do Orçamento:
1. Rendimento: 1 litro de tinta pinta exatamente 3 metros quadrados (3m2
).

2. Embalagem: A tinta só é vendida em latas fechadas de 18 litros, e cada lata custa R$
80,00.
3. O Desafio do Arredondamento (Lógica Condicional 1): Como a loja só vende latas
inteiras, se a quantidade necessária de litros não for uma divisão exata por 18, você
precisará comprar uma lata a mais para cobrir o restante. Exemplo: Se você precisar de
19 litros, uma única lata de 18 litros não será suficiente.
4. Promoção Especial (Lógica Condicional 2): A loja de tintas de Parnamirim é parceira
do IFRN e oferece um desconto de 10% no valor total caso o mutirão compre 3 ou
mais latas.'''
Metros = int(input())
'''1 - 3
  18 - 80  '''
litros = Metros/3
tinta_def = litros /18
if tinta_def % 1 != 0:
	tinta_def = int(tinta_def)+1
else:
	int(tinta_def)
if tinta_def % 1 == 0 and tinta_def<3:
	print(f"valor da tinta: R$ {tinta_def*80:.2f}\nLatas de tinta nescessária(s): {tinta_def}\nLitros de tinta: {litros:.2f}")
else:
	print(f"Valor da tinta: R$ {((tinta_def*80)-(tinta_def*80*(10/100))):.2f}\nLatas de tinta nescessaria(s): {tinta_def}\n Litros de tinta: {litros:.2f}")