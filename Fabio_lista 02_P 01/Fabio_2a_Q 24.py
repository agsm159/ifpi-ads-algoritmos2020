#24.Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
#coeficiente A deve ser diferente de 0 (zero).
from math import sqrt

def main():
    a = int(input('Qual o valor do coeficiente A:'))
    b = int(input('Qual o valor do coeficiente B:'))
    c = int(input('Qual o valor do coeficiente C:'))

    print(calculos(a, b, c))

def calculos(a, b, c):
    delta = b ** 2 - 4 * a * c

    if a != 0:
        x1 = ((-1 * b) + delta) / (2 * a)
        x2 = ((-1 * b) - delta) / (2 * a)
        return "raiz 1: %.2f \nraiz 2: %.2f"%(x1,x2)

    else:
        print('O valor de "A" não pode ser 0')

main()
