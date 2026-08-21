'''Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar.'''
M, P = map(float, input().split())
P = M*(P/100)
print (f"DESCONTO = {P}, {M-P}")