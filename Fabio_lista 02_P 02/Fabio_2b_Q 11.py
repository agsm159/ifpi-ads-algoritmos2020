#11.Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
#número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
#o 326 = 3 centenas, 2 dezenas e 6 unidades
#o 12 = 1 dezena e 2 unidades

def main():
    num = int(input('Digite um número menor que 1000:'))

    verif_quant(num)

def verif_quant(num):
    cent = (num // 100) % 10
    dez = (num // 10) % 10
    uni = (num // 1) % 10

    if num < 1000 and num >= 1:
        if cent <= 1:
            print(f'\n{cent} centena')
        elif cent > 1:
            print(f'\n{cent} centenas')

        if dez <= 1:
            print(f'\n{dez} dezena')
        elif dez > 1:
            print(f'\n{dez} dezenas')

        if uni <= 1:
            print(f'\n{uni} unidade')
        elif uni > 1:
            print(f'\n{uni} unidades')

    else:
        print('Número Inválido')

main()
