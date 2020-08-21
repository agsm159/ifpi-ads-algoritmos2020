def main():
    
    num = int(input('Digite um valor: '))

    cont = 1
    soma = 0

    while num >= 1:
      
        soma = soma + cont / num
        
        num -= 1    
        cont += 1

    print(soma)


main()
