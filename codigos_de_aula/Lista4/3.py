'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento
de 1.5%. Implemente um algoritmo que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''
B, A, COUNT = 80000, 200000, 0
while B<=A:
    if B>=A:
        break
    B+=B*(3/100)
    A+=A*(1.5/100)
    COUNT+=1
print(f"Demorou {COUNT} anos para o país A passar o país B")