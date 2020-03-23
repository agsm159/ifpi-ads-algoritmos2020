#28.Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
#um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
#não pode ser negativo.

def main():
    print('Informe a localização do 1º ponto.\n')

    x1 = int(input('Qual o valor de x1:'))
    y1 = int(input('Qual o valor de y1:'))

    print('\nInforme a localização do 2º ponto.\n')

    x2 = int(input('Qual o valor de x2:'))
    y2 = int(input('Qual o valor de y2:'))

    área_do_retângulo = calculo_área(x1, y1, x2, y2)
    print(f'\n{área_do_retângulo}')

def calculo_área(x1, y1, x2, y2):
    area_retang = (x2 - x1) * (y2 - y1)

    if x1 != x2 and y1 != y2:
        if area_retang < 0:
            area_retang = area_retang * -1
            print(f'Área do retângulo = {area_retang}')

    else:
        print('Localização dos pontos inválidos!')

main()
