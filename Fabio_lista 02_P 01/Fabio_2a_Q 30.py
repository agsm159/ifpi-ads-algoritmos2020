#30.Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
#o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
#milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
#terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
#2025 -> dividindo: 20 e 25 -> somando temos 45 -> 45**2 = 2025.

def main():
    print('Números entre 1000 e 9999 possuem uma característica interresante, vamos ver como funciona.\n')
    num = int(input('Digite um número entre 1000 e 9999:'))

    print(calculos(num))

def calculos(num):
    v1 = num // 100
    v2 = num % 100
    soma = v1 + v2
    raiz = soma ** 2

    if soma ** 2 == num:
        print(f'\nO número {num}, se divido em duas partes com sua milhar e centena formando {v1},\n '
              f'e a dezena com a unidade formando {v2}, se somados resulta em {soma}, cuja soma,\n'
              f'se elevada ao quadrado resulta em {raiz}, o mesmo valor do número {num} escolhido.')
    else:
        print('Tente novamente com um número de 4 algarismos!')

main()
