#13.Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.

def main():
    print('Escreva valores diferentes!')
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))
    n3 = int(input('Digite o terceiro número:'))
    n4 = int(input('Digite o quarto número:'))
    n5 = int(input('Digite o quinto número:'))

    print(f'\nO maior núemro é {maior_numero(n1, n2, n3, n4, n5)} e o menor é {menor_numero(n1, n2, n3, n4, n5)}.')

def maior_numero(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return n1

    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        return n2

    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        return n3

    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        return n4

    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        return n5

def menor_numero(n1, n2, n3, n4, n5):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        return n1

    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        return n2

    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        return n3

    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        return n4

    elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        return n5

main()
