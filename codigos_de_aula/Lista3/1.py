'''1. O Racha da Pizza (com Taxa Opcional)
• Cenário: Você e sua galera do IFRN foram comemorar o fim do bimestre comendo pizza na
Cohabinal. Para não ter estresse na hora de pagar, você vai programar uma calculadora de
divisão.
• A Condição: O programa deve ler o valor total da conta e a quantidade de amigos. Em
seguida, deve perguntar se o grupo deseja pagar a taxa de serviço de 10% do garçom (o
usuário deve responder com "sim" ou "não").
o Se a resposta for "sim", adicione 10% ao valor total antes de fazer a divisão.
o Senão, divida o valor bruto da conta igualmente entre os amigos.
• Saída: Exiba o valor individual que cada um deve pagar formatado com duas casas decimais.'''
Valor_total = int(input("R$ "))
Quantidade_de_amigos = int(input())
Taxa = input("Deseja pagar a taxa de  10%?")
if Taxa.lower() == "Sim":
	print(f"R$ {Valor_total/Quantidade_de_amigos+(((Valor_total/Quantidade_de_amigos) * 10/100))}")
else:
	print(f"R$ {Valor_total/Quantidade_de_amigos}")