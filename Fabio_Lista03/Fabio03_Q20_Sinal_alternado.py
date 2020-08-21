def main():
    
    n = int(input('Digite um valor: '))

    num = 1
    soma = 0

    while num <= n:
      
        if num % 2 != 0:
            soma = soma + 1 / num

        else:
            soma = soma - 1 / num
        
        num += 1

    print(soma)


main()
