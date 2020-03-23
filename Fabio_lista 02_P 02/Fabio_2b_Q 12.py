#12.Leia um número e escreva se o número é inteiro ou decimal.

def main():
    num = float(input('Digite um número:'))

    int_dec(num)

def int_dec(num):
    if num % 1 == 0:
        print('\nEsse número é inteiro')

    else:
        print('\nEsse número é decimal')

main()
