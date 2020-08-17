def main():
    
    cont = 1
    n = int(input('Digite um número: '))
    acumulador = n

    while cont != n:

        acumulador = acumulador + (n - cont)
        cont = cont + 1

    print(acumulador)

main()
