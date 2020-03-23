#25.Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
#uma mensagem de permissão de acesso ou não.

def main():
    print('********* Faça seu login ***********\n')

    print('Login : Rogério123')
    senha = int(input('Senha(casa tenha esquecido é 1234):'))

    print('\n************************************')

    print(permissão(senha))

def permissão(senha):
    if senha == 1234:
        print('Login efetuado com sucesso!')

    else:
        print('Acesso negado!! Verifique sua senha e tente novamente.')

main()
