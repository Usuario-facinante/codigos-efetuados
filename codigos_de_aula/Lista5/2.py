'''Uma turma possui N alunos. Para cada aluno serão informadas duas notas entre 0 e 100. Calcule a média de cada
aluno e classifique-o de acordo com as regras:
• média >= 60 → Aprovado;
• 20 <= média < 60 → Prova Final;
• média < 20 → Reprovado.
Armazene todas as médias em uma lista. Ao final, mostre:
• maior média;
• menor média;
• média geral da turma;
• quantidade de alunos em cada situação;
• percentual de alunos aprovados.
Desafio extra: mostre as médias em ordem decrescente.'''

Alunos = int(input("\nDigite quantos alunos tem na sala"))
media, aprovados, reprovados, prova_final = [], 0, 0, 0
for _ in range (Alunos):
    nota1, nota2 = map(float, input().split())
    media.append((nota1 + nota2)/2)
    if (nota1 + nota2)/2 >= 60:
        aprovados += 1
    elif 60 > (nota1 + nota2)/2 >= 20:
        prova_final += 1
    else:
        reprovados += 1
media.sort(reverse=True)
print(f"\nA média maior: {max(media)}\nA média menor: {min(media)}\nMédia geral: {sum(media)//Alunos}\nA Quantidade de alunos em cada situação é:\n{50*"*"}\nAprovados: {aprovados}\nReprovados: {reprovados}\nProva final: {prova_final}\nPorcentagem de alunos aprovados: {(aprovados/Alunos)*100:.2f}%\nMédias em ordem decrescente:", *media)