def main():
    
    n = int(input('Digite a quantidade de números: '))
    cont = 1
    soma = 0
    num = 0

    while cont <= n:

        num = int(input('Digite um valor: '))
        soma = soma + num
        media = soma / n
        cont = cont + 1

    print(f'A soma dos valores é igual a: {soma}')
    print(f'A média é igual a: {media}')

main()
