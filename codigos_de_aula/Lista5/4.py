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

Nome = list(map((int,input())))
Problemas_resolvidos = list(map((int,input())))
penalidade_total = list(map((int,input())))
maior_problema = None
if Problemas_resolvidos.count(max(Problemas_resolvidos)) > 1: #pegando a quatidade de numeros máximos
    maior_problema = [
        index
        for index, valor in enumerate(Problemas_resolvidos)
        if valor == max(Problemas_resolvidos)]
    if maior_problema:
        
    maior_penalidade = [
        V
        for V in penalidade_total
        if penalidade_total.index(V) in maior_problema
    ]
    maior_penalidade.sort()
    