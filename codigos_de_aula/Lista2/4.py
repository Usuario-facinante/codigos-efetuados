'''Em uma disciplina, o aluno faz 3 provas. A Prova 1 tem peso 2, a Prova 2 tem peso 3 e a Prova 3
tem peso 5. A média para passar é 7,0. Faça um programa que leia as notas da Prova 1 e da
Prova 2. O programa deve calcular e exibir qual é a nota mínima que o aluno precisa tirar na
Prova 3 para atingir a média exata de 7,0.
Dica: O aluno precisará isolar a variável da Prova 3 na fórmula da média ponderada antes de
programar.'''
A, B = map(float, input().split())
print (70-(2*A+3*B)//5)