def main():
    
    cont = 0 
    nf = 0

    n = int(input('Digite um valor: '))

    while cont <= n:
        nf = (n - ( n - cont))
        
        if nf % 2 == 0:
            
            print(nf)
        
        cont = cont + 1

main()
