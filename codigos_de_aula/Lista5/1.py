'''Uma loja possui inicialmente 100 unidades de determinado produto. Durante o dia são registradas N operações. Cada
operação contém um número inteiro: valores positivos representam entrada de produtos no estoque e valores
negativos representam vendas ou retiradas.
Faça um programa que leia N e, em seguida, as N movimentações. Ao final, informe:
• o estoque final;
• o maior estoque registrado durante o dia;
• o menor estoque registrado durante o dia.
Caso alguma operação faça o estoque ficar negativo, o programa deve informar em qual operação isso ocorreu pela
primeira vez e encerrar o processamento das operações seguintes.'''
operacoes = int(input())
estoque, valor_max, valor_min = 100, 100, 100
for _ in range (operacoes):
    valor = int(input())
    estoque += valor
    if estoque < valor_min:
        valor_min = estoque
    if estoque > valor_max:
        valor_max = estoque
    if estoque < 0:
        Valor_error = _
        estoque_error = estoque
        print (f'Estoque negativo na operação {Valor_error+1}.\nEstoque no momento do erro: {estoque_error}')
        break
print (f'Maior estoque registrado: {valor_max}\nMenor estoque registrado: {valor_min}')