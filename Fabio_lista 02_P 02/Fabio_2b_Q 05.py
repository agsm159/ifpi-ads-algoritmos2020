#05.Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
#sempre pelo mais barato.

def main():
    prod_1 = float(input('Qual o valor do 1º produto: R$'))
    prod_2 = float(input('Qual o valor do 2º produto: R$'))
    prod_3 = float(input('Qual o valor do 3º produto: R$'))

    print(comparação(prod_1, prod_2, prod_3))

def comparação(prod_1, prod_2, prod_3):
    if prod_1 < prod_2 and prod_1 < prod_3:
        print('\nO 1º produto é o recomendado a ser comprado.')

    elif prod_2 < prod_1 and prod_2 < prod_3:
        print('\nO 2º produto é o recomendado a ser comprado.')

    elif prod_3 < prod_1 and prod_3 < prod_2:
        print('\nO 3º produto é o recomendado a ser comprado.')

    else:
        print('\nTodos os produtos tem o mesmo preço.')

main()
