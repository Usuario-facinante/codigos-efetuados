'''7. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo
deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.
Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja
em falta no caixa.'''

Conta = int(input("Digite o valor da conta: R$ "))
Valor_dado = int(input("Digite o valor do pagamento efetuado: R$ "))
troco, C, V, D, c, d, u = Valor_dado - Conta, 0, 0, 0, 0, 0, 0
while troco > 0 and troco >= 50:
    troco -= 50
    C += 1
while troco > 0 and troco >= 20:
    troco -= 20
    V += 1
while troco > 0 and troco >= 10:
    troco -= 10
    D += 1
while troco > 0 and troco >= 5:
    troco -= 5
    c += 1
while troco > 0 and troco >= 2:
    troco -= 2
    d += 1
while troco > 0 and troco >= 1:
    troco -= 1
    u += 1
print ("O troco deve ser de exatamente:")
if C != 0:
    print (f"{C} cédula(s) de cinquenta reais.")
if V != 0:
    print (f"{V} cédula(s) de vinte reais.")
if D != 0:
    print (f"{D} cédula(s) de dez reais.")
if c != 0:
    print (f"{c} cédula(s) de cinco reais.")
if d != 0:
    print (f"{d} cédula(s) de dois reais.")
if u != 0:
    print (f"{u} moeda(s) de um reais.")