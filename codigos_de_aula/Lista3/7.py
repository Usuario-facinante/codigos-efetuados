'''7. Validador de Login Seguro (Simulador do SUAP)
• Cenário: Segurança cibernética é essencial. Você precisa criar a lógica de validação de
acesso ao boletim do SUAP.
• A Condição: Defina previamente no código uma string para o usuário padrão (ex: "ifrn2026")
e outra para a senha padrão (ex: "ParnaSuap"). O programa deve pedir para o usuário digitar
seu login e, em seguida, sua senha.
o Se o login E a senha digitados forem idênticos aos valores padrão estabelecidos,
exiba: "Acesso liberado. Bem-vindo ao SUAP!"
o Senão, exiba: "Credenciais inválidas. Acesso bloqueado!"'''
Usuario, Senha = "Usuario-fascinante", "Senha_confiavel@0_0"
Usuario_requisição = input("Usuário: ")
Senha_requisição = input("Senha: ")
if Usuario == Usuario_requisição and Senha == Senha_requisição: 
	print("Acesso liberado. Bem-vindo ao SUAP!") 
else: 
	print("Credenciais inválidas. Acesso bloqueado!")