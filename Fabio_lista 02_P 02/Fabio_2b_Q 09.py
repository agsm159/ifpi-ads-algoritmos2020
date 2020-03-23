#09.Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro
#valor deve aparecer valor inválido.

def main():
    dia_sem = int(input('Digite um dia:'))

    dia_correspondente(dia_sem)

def dia_correspondente(dia_sem):
    if dia_sem == 1:
        print('Essa data é um Domingo.')

    elif dia_sem == 2:
        print('Essa data é uma Segunda.')

    elif dia_sem == 3:
        print('Essa data é uma Terça.')

    elif dia_sem == 4:
        print('Essa data é uma Quarta.')

    elif dia_sem == 5:
        print('Essa data é uma Quinta.')

    elif dia_sem == 6:
        print('Essa data é uma Sexta.')

    elif dia_sem == 7:
        print('Essa data é um Sábado.')

    else:
        print('Valor inválido!')

main()
