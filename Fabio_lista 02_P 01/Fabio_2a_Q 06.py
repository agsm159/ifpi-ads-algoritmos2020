#06.Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
#se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
#verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
#obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

def main():
    ang1 = int(input('Digite um valor para o primeiro ângulo:'))
    ang2 = int(input('Digite um valor para o segundo ângulo:'))
    ang3 = int(input('Digite um valor para o terceiro ângulo:'))

    verif_triag(ang1, ang2, ang3)

def verif_triag(ang1, ang2, ang3):
    if ang1 + ang2 + ang3 != 180:
        print('Não  é possivel formar um triângulo com os valores apresentados.')

    else:
        if ang1 < 90 and ang2 < 90 and ang3 < 90:
            print('Os valores apresentados correspondem a um triângulo acutângulo .')

        if ang1 == 90 or ang2 == 90 or ang3 == 90:
            print('Os valores apresentados correspondem a um triângulo retângulo.')

        if ang1 > 90 or ang2 > 90 or ang3 > 90:
            print('Os valores apresentados correspondem a um triângulo obtusângulo.')

main()
