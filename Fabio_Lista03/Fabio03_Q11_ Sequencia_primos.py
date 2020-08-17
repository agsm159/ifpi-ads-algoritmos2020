def main():
    import math

    inicio = int(input('Digite o número inicial da sequência númerica: '))
    fim = int(input('Digite o número final da sequência númerica: '))

    cont = inicio

    while cont <= fim:

        if cont == 2:
            print(cont)
        
        elif cont % 2 != 0:

            if cont == 3 or cont == 5 or cont == 7 or cont == 11 or cont == 13 or cont == 17:
                print(cont)

            elif cont % 3 != 0 and cont % 5 != 0 and cont % 7 != 0 and cont % 11 != 0 and cont % 13 != 0 and cont % 17 != 0:
                print(cont)

        
        cont = cont + 1


main()
