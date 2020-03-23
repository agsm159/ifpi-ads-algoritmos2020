#14.Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#1. Álcool:
#· até 20 litros, desconto de 3% por litro
#· acima de 20 litros, desconto de 5% por litro
#2. Gasolina:
#· até 20 litros, desconto de 4% por litro
#· acima de 20 litros, desconto de 6% por litro.
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
#seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
#o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def main():
    print('Escolha o tipo de combustível:\n')
    print('A - álcool             preço por litro: R$1.90')
    print('G - gasolina           preço por litro: R$2.50')
    tipo = input('\nTipo desejado: ')
    quant = float(input('Quantos litros você deseja colocar: '))

    pagamento(tipo, quant)

def pagamento(tipo, quant):
    preço_gas = quant * 2.5
    preço_alc = quant * 1.9

    if tipo == 'A':
        if quant <= 20:
            desc_alc = quant * 3 / 100
            total = preço_alc - desc_alc
            print(f'\nValor a ser pago: R${total:.2f} ')

        elif quant > 20:
            desc_alc = quant * 5 / 100
            total = preço_alc - desc_alc
            print(f'\nValor a ser pago: R${total:.2f} ')

    elif tipo == 'G':
        if quant <= 20:
            desc_gas = quant * 4 / 100
            total = preço_alc - desc_gas
            print(f'\nValor a ser pago: R${total:.2f} ')

        elif quant > 20:
            desc_gas = quant * 6 / 100
            total = preço_alc - desc_gas
            print(f'\nValor a ser pago: R${total:.2f} ')

    else:
        print('Tipo inválido.')

main()
