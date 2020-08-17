def main():
    cont = 1

    print('Escolha a operação desejada.\n' )
    print('1 - Adição | 2 - Subtração | 3 - Multiplicação | 4 - Divisão')

    t = int(input('Digite o número correspondente ao tipo de operação: '))
    n = int(input('Digite o número desejado: '))

    while cont <= 10:

        if t == 1:
            
            tab = n + cont
            print(f'{n} + {cont} = {tab}')
            cont = cont + 1

        elif t == 2:
            
            tab = n - cont
            print(f'{n} - {cont} = {tab}')
            cont = cont + 1

        elif t == 3:
            tab = n * cont
            print(f'{n} * {cont} = {tab}')
            cont = cont + 1
        
        elif t == 4:
            tab = n / cont
            print(f'{n} / {cont} = {tab}')
            cont = cont + 1

        else:
            print('Operação Inválida!')
main()
