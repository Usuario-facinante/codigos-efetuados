'''Implemente um algoritmo que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''
Nome_de_usuario = input("Digite o nome de usuário: ")
Senha = input("Digite a senha: ")
while Senha == Nome_de_usuario:
    print("A senha não pode ser igual ao nome de usuário. Digite novamente.")
    Senha = input("Digite a senha: ")