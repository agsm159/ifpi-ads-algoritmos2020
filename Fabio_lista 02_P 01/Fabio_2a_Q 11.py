#11.Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
#valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
#possíveis para a variável opção são 1, 2 e 3.

def main():
    opção = int(input('Escolha e digite um dos seguintes valores( 1, 2 ou 3):'))
    num1 = int(input('Digite o primeiro número:'))
    num2 = int(input('Digite o segundo número:'))
    num3 = int(input('Digite o terceiro número:'))

    rescrever_valor(opção, num1, num2, num3)

def rescrever_valor(opção, num1, num2, num3):
    if opção == 1:
        print(f'O valor escolhido é {num1}.')

    elif opção == 2:
        print(f'O valor escolhido é {num2}.')

    elif opção == 3:
        print(f'O valor escolhido é {num3}.')

    else:
        print('Não é possivel estabeler um resultado, tente novamente.')

main()