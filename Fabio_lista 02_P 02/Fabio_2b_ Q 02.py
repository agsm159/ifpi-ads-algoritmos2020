#02.Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.

def main():
    sexo = input('Qual o seu sexo?(F ou M)\n')

    print(masc_fem(sexo))

def masc_fem(sexo):
    if sexo == 'F':
        print('\nVocê é dos sexo feminino.')

    elif sexo == 'M':
        print('\nVocê é dos sexo masculino.')


    else:
        print('Sexo inválido.')

main()
