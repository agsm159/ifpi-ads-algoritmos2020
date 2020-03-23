#19.Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
#(IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25),
#obeso (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

def main():
    h = float(input('Qual a sua altura (em metros)?\n'))
    peso = float(input('Quanto você pesa(em kg)?\n'))

    def_imc(h, peso)

def def_imc(h, peso):
    imc = peso / h ** 2

    if imc < 25 and imc > 18.5:
        print('\nO seu peso está normal.')

    elif imc > 25 and imc < 30:
        print('\nVocê está obeso.')

    elif imc > 30:
        print('\nVocê está com obesidade mórbida.')

    elif imc < 18.5:
        print('\nVocê está abaixo do peso.')

main()
