'''Faça um programa que pergunte quanto um profissional ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário bruto. Em seguida, calcule e exiba
os descontos abaixo, bem como o salário líquido final:
a. Imposto de Renda (11% do bruto)
b. INSS (8% do bruto)
c. Sindicato (5% do bruto)
d. Salário Líquido (Bruto menos todos os descontos)'''
H, NH = map(int, input().split())
A = H*NH-((H*NH)*11/100)
print (f"{H*NH}\n{H*NH-((H*NH)*11/100)}\n{H*NH-((H*NH)*8/100)}\n{H*NH-((H*NH)*5/100)}\n{H*NH-((H*NH)*24/100)}")
