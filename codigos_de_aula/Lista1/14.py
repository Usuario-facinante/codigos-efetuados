'''14. O Índice de Massa Corporal (IMC) é uma fórmula utilizada para verificar se um adulto está no
seu peso ideal. Faça um programa que peça o peso (em kg) e a altura (em metros) do usuário.
Calcule e imprima o IMC dele na tela.'''
KG, A = map(int, input().split())
print (KG/A**2)