'''Um aluno quer saber quanto dinheiro terá no futuro se investir suas economias. Faça um
programa que peça o valor inicial investido (Capital), a taxa de juros mensal (i, em porcentagem)
e a quantidade de meses (t) que o dinheiro ficará rendendo. Calcule e exiba o Montante final e
o Lucro (apenas os juros gerados).'''
C, I, T = map(float, input().split())
print (f" montante = {C*(1+((I/100)**T))} JUROS = {(C*(1+((I/100)**T)))-C}")