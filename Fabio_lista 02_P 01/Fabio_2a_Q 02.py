#02.Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

def main():
    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro número:'))

    verif_menor_maior(n1, n2)

def verif_menor_maior(n1, n2):
    if n1 > n2:
        print(f'O número {n1} é maior que o número {n2}.')
    else:
        print(f'O número {n1} é menor que o número {n2}.')

main()
