#18.Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
#Adição , 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
#sobre os dois valores lidos.

def main():
    num1 = int(input('Digite um valor:'))

    print('\nQual das operações deseja realizar:\n1 - Adiação\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')

    operaçao = int(input('Qual a operação escolhida?\n'))

    num2 = int(input('Digite outro valor:'))

    resultado = calculos(num1, operaçao, num2)
    print(resultado)


def calculos(num1, operaçao, num2):
    if operaçao == 1:
        print('O valor da soma é:', num1 + num2)

    elif operaçao == 2:
        print('O valor da subtraçao é:',num1 - num2)

    elif operaçao == 3:
        print('O valor da multiplicação é:',num1 * num2)

    elif operaçao == 4:
        if num2 != 0:
            print('O valor da divisão é:',num1 / num2)
        else:
            ('Não é possivel realizar uma divisão por zero')

    else:
        print(f'\nA opção {operaçao} é inválida.')

main()
