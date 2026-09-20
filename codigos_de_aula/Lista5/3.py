saldo = int(input("Saldo inicial R$ ")); suspeitas, transacoes_total = [], []
count = int(input("Quantidade de transações desejadas:\n"))
print("Trasações:")
for i in range (count):
    transacoes = int(input())
    transacoes_total.append(transacoes)
    saldo += transacoes
    if i >=2:
        if transacoes_total[i] < 0 and transacoes_total[i-1] < 0 and transacoes_total[i-2] < 0:
            for x in range (i -2, i +1):
                if transacoes_total[x] < 0:
                    if transacoes_total[x] not in suspeitas:
                        suspeitas.append(transacoes_total[x])
    if transacoes_total[i] < -5000  or transacoes_total[i] > 5000:
        suspeitas.append(transacoes)
    if saldo < 0:
        suspeitas.append(transacoes)
print("Houve as seguintes transações suspeitas:\n")
print(suspeitas)
