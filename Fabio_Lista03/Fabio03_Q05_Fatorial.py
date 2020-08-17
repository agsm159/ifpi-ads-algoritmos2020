def main():
    n = int(input('Digite um número: '))
    cont = n

    while cont != 1:
        cont = cont - 1
        n = n * cont

    print(n)

main()
