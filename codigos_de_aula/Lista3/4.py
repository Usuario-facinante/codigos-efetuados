'''Filtro de Spam e Textos Curtos no Discord
• Cenário: Você está programando um bot moderador para o servidor de Discord da sua turma
do IFRN. O bot precisa validar o tamanho das mensagens enviadas no chat de avisos
importantes.
• A Condição: Leia a mensagem digitada pelo usuário. Usando a função len(), verifique o
comprimento do texto:
o Se o tamanho do texto for menor que 3 caracteres OU maior que 140 caracteres,
exiba: "Mensagem bloqueada por violar as diretrizes de spam!"
o Senão, exiba: "Mensagem enviada com sucesso!"'''
Mensagem = input()
if 3>len(Mensagem) or 140<len(Mensagem):
	print("Mensagem bloqueada por violar as diretrizes de spam!")
else:
	print("Mensagem enviada com sucesso!")