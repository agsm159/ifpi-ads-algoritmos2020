#17.Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
#escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
#escreva o quadrado dos números lidos.

def main():
    num_1 = int(input('Digite o primeiro valor:'))
    num_2 = int(input('Digite o segundo valor:'))

    resto = num_1 % num_2

    opçoes(num_1, num_2, resto)

def opçoes(num_1, num_2, resto):
    if resto == 1:
        print(f'A soma de {num_1} e {num_2} mais o resto da divisão dos mesmos é',num_1 + num_2 + 1,'.')

    elif resto == 2:
        if num_1 % 2 == 0 and num_2 % 2 == 0:
            print(f'Os números {num_1} e {num_2} são par.')

        elif num_1 % 2 == 0 and num_2 % 2 != 0:
            print(f'O número {num_1} é par e o {num_2} é ímpar.')

        elif num_1 % 2 != 0 and num_2 % 2 == 0:
            print(f'O número {num_2} é par e o {num_1} é ímpar.')

        else:
            print(f'Os números {num_1} e {num_2} são ímpar.')

    elif resto == 3:
        if (num_1 + num_2) * num_1:
            print(f'A soma entre {num_1} e {num_2}, vezes {num_1} é',(num_1 + num_2) * num_1,'.' )

    elif resto == 4:
        if (num_1 + num_2) / num_2:
            print(f'A soma entre {num_1} e {num_2}, dividido por {num_2} é',(num_1 + num_2) / num_2,'.' )

    elif resto != 0:
        print(f'O quadrado de {num_1} é', num_1 ** 2,f'e o quadrado de {num_2} é', num_2 ** 2,'.')

main()
