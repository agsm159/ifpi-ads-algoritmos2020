#01.Leia um número e mostre na tela se o número é positivo ou negativo.

def main():
    num = int(input('Digite um número:'))

    print(positivo_ou_negativo(num))

def positivo_ou_negativo(num):
    if num > 0:
        print(f'O número {num} é positivo.')

    else:
        print(f'O número {num} é negativo.')

main()
