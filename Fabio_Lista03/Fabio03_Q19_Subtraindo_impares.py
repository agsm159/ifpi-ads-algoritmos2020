def main():
    
    n = int(input('Digite um valor: '))

    num = 1
    soma = 0

    while n >= 1:
      
        if num % 2 != 0:
            soma = soma + num / n

        else:
            soma = soma - n / num
        
        n -= 1    
        num += 1

    print(soma)


main()
