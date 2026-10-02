'''Em uma competição participaram N estudantes. Para cada participante são informados:
• nome;
• quantidade de problemas resolvidos;
• tempo total de penalidade.
O melhor participante é aquele que resolveu a maior quantidade de problemas. Em caso de empate, vence aquele que
possui a menor penalidade.
Use três listas paralelas para armazenar os dados.
Ao final, apresente:
• campeão;
• quantidade de problemas resolvidos;
• penalidade;
• quantidade de participantes que resolveram pelo menos um problema;
• média de problemas resolvidos.
Desafio: apresente o ranking completo.'''

Nome = list(input().split())
Problemas_resolvidos = list(map(int,input().split()))
penalidade_total = list(map(int,input().split()))
penalidade_max_rep = []
maior_problema = None
campeoes = []
if Problemas_resolvidos.count(max(Problemas_resolvidos)) > 1: #pegando a quantidade de numeros máximos
    maior_problema = [
        index
        for index, valor in enumerate(Problemas_resolvidos)
        if valor == max(Problemas_resolvidos)
        ]
    maior_penalidade = [
        penalidade
        for index, penalidade in enumerate(penalidade_total)
        if index in maior_problema
        ]
    maior_penalidade.sort()
    penalidade = maior_penalidade[0]
    campeao = penalidade_total.index(penalidade)
    if penalidade[0] == penalidade[1]:
        for x in range (len(penalidade)):
            if penalidade[x] == penalidade[x-1]:
                penalidade_max_rep.append()
        for i in range (len(penalidade_max_rep)):
            campeoes.append(penalidade_total.index(penalidade_max_rep[i]))
            campeoes = penalidade_total.index(campeoes[i])
        campeao = campeoes
        resolucao = [
            maior_que_0
            for maior_que_0 in Problemas_resolvidos
            if maior_que_0 > 0
        ]
else:
    campeao = Problemas_resolvidos.index(max(Problemas_resolvidos))
print(f"Campeão: {Nome[campeao]}\nQuantidade de problemas resolvidos: {max(Problemas_resolvidos)}\nPenalidades: {penalidade_total[campeao]}\nParticipantes que resolveram ao menos um problema: {resolucao}\nMédia de problemas resolvidos: {sum(Problemas_resolvidos)/len(Problemas_resolvidos)}")