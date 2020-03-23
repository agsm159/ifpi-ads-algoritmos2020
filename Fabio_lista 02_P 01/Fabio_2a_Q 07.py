#.07Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
#(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
#formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

def main():
    lado_1 = int(input('Digite o valor do primeiro lado:'))
    lado_2 = int(input('Digite o valor do segundo lado:'))
    lado_3 = int(input('Digite o valor do terceiro lado:'))

    tipo_lado(lado_1, lado_2, lado_3)

def tipo_lado(lado_1, lado_2, lado_3):
    if lado_1 + lado_2 < lado_3:
        print('Não é possivel formar um triângulo.')

    else:
        if lado_1 == lado_2 == lado_3:
            print('É possivel formar um triângulo equilátero.')

        if (lado_1 == lado_2) != lado_3  or (lado_1 == lado_3) != lado_2 or (lado_2 == lado_3) != lado_1:
            print('É possivel formar um triângulo isósceles.')

        if lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
            print('É possivel formar um triângulo escaleno.')

main()
