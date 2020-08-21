def main():
    
    num = int(input('Digite um valor: '))

    cont = 1
    soma = 0

    while cont <= num:
      
        soma = soma + 1 / cont

        cont += 1

    print(soma)


main()
