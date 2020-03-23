#23.Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.

def main():
    print('Determine a primeira data:\n')
    dia_1 = int(input('Qual o dia da primeira data:'))
    mes_1 = int(input('Qual o mês da primeira data:'))
    ano_1 = int(input('Qual o ano da primeira data:'))

    print('\nDetermine a segunda data:\n')
    dia_2 = int(input('Qual o dia da segunda data:'))
    mes_2 = int(input('Qual o mês da segunda data:'))
    ano_2 = int(input('Qual o ano da segunda data:'))

    mais_recente = data_mais_recente(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2)
    print({mais_recente})

def data_mais_recente(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2):
    mes_val = mes_1 >= 1 and mes_1 <= 12 and mes_2 >= 1 and mes_2 <= 12
    dia_val = dia_1 >= 1 and dia_1 <= 30 and dia_2 >= 1 and dia_2 <= 30
    if mes_val and dia_val:
        if ano_1 > ano_2:
            print(f'\nA primeira data {dia_1}/{mes_1}/{ano_1} é mais recente.')

        elif ano_1 < ano_2:
            print(f'\nA segunda data {dia_2}/{mes_2}/{ano_2} é mais recente.')

        else:
            if mes_1 > mes_2:
                print(f'\nA primeira data {dia_1}/{mes_1}/{ano_1} é mais recente.')

            elif mes_1 < mes_2:
                print(f'\nA segunda data {dia_2}/{mes_2}/{ano_2} é mais recente.')

            else:
                if dia_1 > dia_2:
                    print(f'\nA primeira data {dia_1}/{mes_1}/{ano_1} é mais recente.')

                elif dia_1 < dia_2:
                    print(f'\nA segunda data {dia_2}/{mes_2}/{ano_2} é mais recente.')

    else:
        print('!!! Data inválida !!!')

main()
