#06.Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
#escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def main():
    print('Em qual turno você estuda?\n M - Matutino\n V - Vespertino\n N - Noturno')

    turno = str(input('\nTurno:'))
    print(comprimento(turno))

def comprimento(turno):
        if turno == 'M':
            print('\nBom dia!')

        elif turno == 'V':
            print('\nBoa Tarde!')

        elif turno == 'N':
            print('\nBoa Noite!')

        else:
            print('\nValor inválido!')

main()
