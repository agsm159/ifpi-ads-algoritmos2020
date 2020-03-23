#10.Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.
def main():
    dia = int(input('Digite um valor o dia:'))
    mes = int(input('Digite um número do mês:'))
    ano = int(input('Digite um ano:'))

    verif_data(dia, mes, ano)

def verif_data(dia, mes, ano):
    if 0 < dia and dia < 30:
        if 0 < mes and mes < 12:
            print(f'A data {dia}/{mes}/{ano} é valida.')

    else:
      print(f'A data {dia}/{mes}/{ano} não é valida.')

main()
