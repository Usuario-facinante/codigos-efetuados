'''19. Um aluno deseja organizar sua rotina. Faça um programa que pergunte quantas horas livres por
semana ele tem no total e quantas disciplinas ele está cursando neste semestre. O programa
deve reservar, por padrão, 3 horas semanais desse tempo total para imprevistos/descanso, e
então dividir o tempo restante igualmente entre as disciplinas. Exiba quantas horas ele deve
dedicar para cada matéria.'''
HL, D = map(int, input().split())
print ((HL-3)/D)