#08.Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
#sua idade exata (em anos).

def main():
    dia = int(input('Digite o número do dia atual?'))
    mes = int(input('Digite o número do mês atual?'))
    ano = int(input('Digite o ano do mês atual?'))

    dia_nas = int(input('Em qual dia você nasceu?'))
    mes_nas = int(input('Qual o número do mês que você nasceu?'))
    ano_nas = int(input('Em qual ano você nasceu?'))

    idade_correspodente(dia, mes, ano, dia_nas, mes_nas, ano_nas)

def idade_correspodente(dia, mes, ano, dia_nas, mes_nas, ano_nas):
    idade_estimada = ano - ano_nas

    if mes < mes_nas:
        print(f'Sua idade estimada é {idade_estimada - 1} anos.')
    elif mes > mes_nas:
        print(f'Sua idade estimada é {idade_estimada} anos.')
    else:
        if dia < dia_nas:
            print(f'Sua idade estimada é {idade_estimada - 1} anos.')
        elif dia > dia_nas:
            print(f'Sua idade estimada é {idade_estimada} anos.')

main()
