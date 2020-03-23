#29.Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
#formadas pelos seus dois primeiros e dois últimos dígitos.
#Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
#Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

def main():
    num = int(input('Digite um número de 4 dígitos:'))

    print(verif_q_p(num))

def verif_q_p(num):

    raiz_quad = num ** 0.5
    first_digito = num // 100
    last_digito = num - first_digito * 100
    soma_total = first_digito + last_digito

    if raiz_quad == soma_total:
        print(f'\nO número {num} é um quadrado perfeito.')

    else:
        print(f'\nO número {num} não é um quadrado perfeito.')

main()
