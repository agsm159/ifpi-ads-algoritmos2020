#20.Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou quarto)
#em que o ângulo se localiza.

def main():
    ang = int(input('Digite uma medida de um ângulo(entre 0 e 360°):\n'))

    quadrante(ang)

def quadrante(ang):
    if ang < 0 or ang > 360:
        print('Ângulo inválido, tente novamente.')

    else:
        if ang < 90:
            print('Esse ângulo pertence ao primeiro quadrante.')

        elif ang < 180:
            print('Esse ângulo pertence ao segundo quadrante.')

        elif ang < 270:
            print('Esse ângulo pertence ao terceiro quadrante.')

        else:
            print('Esse ângulo pertence ao quarto quadrante.')

main()
