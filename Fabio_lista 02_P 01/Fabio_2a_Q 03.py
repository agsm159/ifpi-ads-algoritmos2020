#03.Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

def main():
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))
    n3 = int(input('Digite o terceiro número:'))

    verif_maior_num(n1, n2, n3)

def verif_maior_num(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f'O maior número é {n1}.')

    elif n2 > n1 and n2 > n3:
        print(f'O maior número é {n2}.')

    elif n3 > n1 and n3 > n2:
        print(f'O maior número é {n3}.')

    else:
        print('Todos os números são iguais.')

main()
