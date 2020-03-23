#14Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

def main():
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))
    n3 = int(input('Digite o terceiro número:'))
    n4 = int(input('Digite o quarto número:'))
    n5 = int(input('Digite o quinto número:'))

    media = (n1 + n2 + n3 + n4 + n5) / 5

    maior_num = maior_que_a_media(n1, n2, n3, n4, n5, media)

    print('\nSão os números maiores que a média.')
    print({maior_num})

def maior_que_a_media(n1, n2, n3, n4, n5, media):

    print(f'A valor da média é {media}.')

    if n1 > media:
        print(n1, end=' ')

    elif n2 > media:
        print(n2, end=' ')

    elif n3 > media:
        print(n3, end=' ')

    elif n4 > media:
        print(n4, end=' ')

    elif n5 > media:
        print(n5, end=' ')
    else:
        print('\nNenhum número está acima da média.')
main()
