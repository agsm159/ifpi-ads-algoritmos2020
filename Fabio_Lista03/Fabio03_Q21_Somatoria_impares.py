def main():

    num = 1
    den = 1
    soma = 0
    cont = 1

    while cont <= 50:
            
        soma += num / den

        
        num += 2
        den += 1
        cont += 1

    print(f'S = {soma}')


main()
