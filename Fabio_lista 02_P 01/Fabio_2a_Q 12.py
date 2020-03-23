#12.Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def main():
    num = int(input('Digite um número qualquer:'))

    impar_par(num)

def impar_par(num):
    if num % 2 == 0:
        print(f'Esse número {num} é par.')

    else:
        print(f'Esse número {num} é impar.')

main()
