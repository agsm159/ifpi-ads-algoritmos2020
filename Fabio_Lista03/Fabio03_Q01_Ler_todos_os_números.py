def main():
    
    cont = 1 
    nf = 0

    n = int(input('Digite um valor: '))

    while cont <= n:

        nf = (n - ( n - cont))
        print(nf)
        cont = cont + 1

main()
