'''Implemente um algoritmo que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.'''
Nota = 0
while Nota < 0 or Nota > 10:
    Nota = float(input("Digite a nota do aluno (0 a 10): "))
    if Nota < 0 or Nota > 10:
        print("Nota inválida. Digite novamente.")
print("Nota válida:", Nota)