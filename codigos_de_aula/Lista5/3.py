'''Um banco registra as movimentações de uma conta durante um dia. O saldo inicial é informado pelo usuário e, em
seguida, são informadas N transações. Valores positivos representam depósitos e valores negativos representam
pagamentos ou saques.
Uma movimentação deve ser considerada suspeita quando ocorrer pelo menos uma das situações:
• valor absoluto da movimentação maior que R$ 5.000,00;
• saldo da conta ficar negativo;
• ocorrerem três retiradas consecutivas.
Faça um programa que processe todas as transações e informe o número de cada transação suspeita.
Ao final, mostre o saldo final e a quantidade total de transações suspeitas.
Exemplo:
Saldo inicial: 8000
Transações:
-500
-700
-400
3000
-6000
O programa deverá identificar tanto a terceira retirada consecutiva quanto a movimentação
superior a R$ 5.000,00.'''

saldo = int(input("Saldo inicial R$ "))
suspeitas = []
transacoes_total = [] 
suspeitas_neg = []
n = 1
count = int(input("Quantidade de transações desejadas:\n"))
print("Trasações:")
for i in range (count):
    transacoes = int(input())
    transacoes_total.append(transacoes)
    saldo += transacoes
    if transacoes_total[i] < -5000  or transacoes_total[i] > 5000:
        suspeitas.append(transacoes)
    if saldo < 0:
        suspeitas.append(transacoes)
        break
if i >=2:
    for x in range (count):
        if transacoes_total[x] < 0 and transacoes_total[x-1] < 0 and transacoes_total [x+1] < 0:
            suspeitas_neg.append(transacoes_total[x])
    if len(suspeitas_neg) > 2:
        suspeitas.append(suspeitas_neg[0])
suspeitas.reverse()
print(f"\nHouve {len(suspeitas)} transações suspeitas:\n")
for suspeita in suspeitas:
    print (f"{n}. {suspeita}")
    n += 1
print (f"\nSaldo final: {saldo}")