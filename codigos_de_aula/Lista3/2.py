'''Upgrade de Skin no Free Fire ou Fortnite
• Cenário: Uma nova skin lendária por tempo limitado entrou na loja do seu jogo favorito! Você
precisa verificar se o seu saldo de moedas virtuais (diamantes/V-Bucks) é suficiente para a
compra.
• A Condição: O programa deve ler o seu saldo de moedas e o preço da skin.
o Se você tiver moedas suficientes, exiba: "Compra realizada! Aproveite sua nova skin."
e mostre o seu novo saldo restante.
o Senão, exiba: "Saldo insuficiente! Faltam X moedas para você comprar este item."
(onde X é a diferença exata que falta).'''
Saldo, Skin = map(float,input().split())
if Saldo>=Skin:
	print(f"Compra realizada! Aproveite sua nova skin. Saldo restante: {Saldo-Skin}")
else:
	print(f"Saldo insuficiente! Faltam {Skin-Saldo} moeda(s) para você comprar este item.")