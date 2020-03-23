#05.Leia 3 (três) números e escreva-os em ordem crescente.

def main():
    n1 = float(input('Digite um número:'))
    n2 = float(input('Digite outro número:'))
    n3 = float(input('Digite mais outro número:'))

    ordem_cresc(n1, n2, n3)

def ordem_cresc(n1, n2, n3):
    if n1 > n2 > n3:
        print(f'Os números em ordem crescente são ({n3}, {n2}, {n1}).')

    elif n1 > n3 > n2:
        print(f'Os números em ordem crescente são ({n2}, {n3}, {n1}).')

    elif n2 > n1 > n3:
        print(f'Os números em ordem crescente são ({n3}, {n1}, {n2}).')

    elif n2 > n3 > n1:
        print(f'Os números em ordem crescente são ({n1}, {n3}, {n2}).')

    elif n3 > n1 > n2:
        print(f'Os números em ordem crescente são ({n2}, {n1}, {n3}).')

    elif n3 > n2 > n1:
        print(f'Os números em ordem crescente são ({n1}, {n2}, {n3}).')

main()
