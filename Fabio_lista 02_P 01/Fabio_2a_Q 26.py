#26.Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

def main():
    print('Digite o tamanho dos lados de um triângulo.\n')

    lado_1 = int(input('Qual o tamanho do 1º lado:'))
    lado_2 = int(input('Qual o tamanho do 2º lado:'))
    lado_3 = int(input('Qual o tamanho do 3º lado:'))

    catetos_e_hipotenusa(lado_1, lado_2, lado_3)

def catetos_e_hipotenusa(lado_1, lado_2, lado_3):
    if lado_1 > lado_2 and lado_1 > lado_3:
        print(f'\nO 1º lado é a hipotenusa e os 2º e 3º lado são os catetos.')

    elif lado_2 > lado_1 and lado_2 > lado_3:
        print(f'\nO 2º lado é a hipotenusa e os 1º e 3º lado são os catetos.')

    elif lado_3 > lado_1 and lado_3 > lado_2:
        print(f'\nO 3º lado é a hipotenusa e os 1º e 2º lado são os catetos.')

    else:
        print('\nTodos os lados são iguais, logo não há hipotenusa.')

main()
