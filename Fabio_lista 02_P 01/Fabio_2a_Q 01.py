#01.Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

def main():
    n1 = int(input('Digito o primeiro número:'))
    n2 = int(input('Digito o segundo número:'))
    n3 = int(input('Digito o terceiro número:'))

    verif_igualdade(n1, n2, n3)

def verif_igualdade(n1, n2, n3):
    if (n1 == n2 == n3):
        print('Os três números são iguais.')

    elif (n1 == n2 or n1 == n3 or n2 == n3):
        print('Existem dois números iguais.')

    else:
        print('Não há números iguais.')

main()
