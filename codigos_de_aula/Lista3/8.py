'''O Desconto Secreto no Açaí do Centro
• Cenário: Para incentivar os alunos a comprarem potes maiores, uma famosa açaíteria perto
do IFRN Parnamirim resolveu dar um desconto agressivo baseado no peso do pote.
• A Condição: O programa deve ler o peso do açaí em gramas. O preço padrão do açaí é de
R$ 0,05 por grama. Calcule o valor bruto (peso * 0.05).
o Se o peso do pote for superior a 500 gramas, aplique um desconto de 15% sobre o
valor bruto e exiba: "Você ganhou 15% de desconto! Valor final: R$ X"
o Senão, exiba: "Valor da compra: R$ X" (sem desconto).'''
Gramas = int(input())
if Gramas>500:
	print(f"Você ganhou 15% de desconto! Valor final: R$ {(Gramas*0.05 + ((Gramas*0.05)*15/100)):.2f}")
else:
	print(f"Valor da compra: R$ {Gramas*0.05:.2f}")