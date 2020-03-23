#04.Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
#do algarismo da unidade.

def main():
    num = int(input('Digite um número de dois digitos:'))
    dez = (num // 10) % 10
    uni = (num % 10) % 10
    verif_dez_igual_dif_uni(num, dez, uni)

def verif_dez_igual_dif_uni(num, dez, uni):
    if dez != uni:
        print('O algorismo da dezena é diferente ao da unidade.')

    else:
        print('O algorismo da dezena é igual ao da unidade.')

main()
