def main():

    n = int(input('Digite um número: '))
    inicio = int(input('Digite o número inicial da sequência númerica: '))
    fim = int(input('Digite o número final da sequência númerica: '))

    cont = inicio

    while cont <= fim:

        if cont % 2 == 0:
            print(cont)

        cont = cont + 1

main()
