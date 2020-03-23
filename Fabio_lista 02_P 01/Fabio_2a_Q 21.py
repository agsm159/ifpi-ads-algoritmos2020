#21.Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
#maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
#contrario, é arredondado para o inteiro imediatamente inferior.

def main():
    num = float(input('Digite um valor decimal:'))

    num_int = int(num // 1)
    num_dec = num - num_int
    aprox = arredondamento(num)

    print(f'O número {num} arredondado é {aprox}')

def arredondamento(num):
    num_int = int(num / 1)
    num_dec = num - num_int

    if num_dec >= 0.5:
        print(num_int + 1)

    else:
        print(num_int - 1)

main()
