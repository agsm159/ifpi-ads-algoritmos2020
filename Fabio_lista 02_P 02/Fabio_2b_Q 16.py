#16.O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#         Até 5 Kg          Acima de 5 Kg
#File    R$ 4,90 por Kg   R$ 5,80 por Kg
#Alcatra R$ 5,90 por Kg   R$ 6,80 por Kg
#Picanha R$ 6,90 por Kg   R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
#cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
#e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
#compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def main():
    print('Escolha somente um dos seguintes tipos de carne para comprar.\n')
    print('File')
    print('Alcantra')
    print('Picanha')

    tipo = input('\nDigite a letra inicial da carne desejada:\n')
    quant = int(input('Quantos quilos deseja comprar:\n'))
    cartao = input('Deseja compar com cartão Tabajara?("S" para sim, "N" para não)\n ')

    print('********** CUPOM FISCAL**********\n')
    pagamento(tipo, quant, cartao)
    print('\n*********************************')

def pagamento(tipo, quant, cartao ):
    if tipo == 'F':
        if quant <= 5:
            if cartao == 'N':
                total = quant * 4.9
                print(f'Tipo:      File ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Á vista')
                print('Valor do desconto:     Insento')
                print(f'Valor a pagar:        R${total:.2f}')
            elif cartao == 'S':
                total = quant * 4.9
                novo_total = total * 5 / 100
                print(f'Tipo:      File ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Cartão Tabajara')
                print('Valor do desconto:     5 %')
                print(f'Valor a pagar:        R${total:.2f}')

        elif quant > 5:
            if cartao == 'N':
                total = quant * 5.8
                print(f'Tipo:      File ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Á vista')
                print('Valor do desconto:     Insento')
                print(f'Valor a pagar:        R${total:.2f}')
            elif cartao == 'S':
                total = quant * 5.8
                novo_total = total * 5 / 100
                print(f'Tipo:      File ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Cartão Tabajara')
                print('Valor do desconto:     5 %')
                print(f'Valor a pagar:        R${total:.2f}')

    elif tipo == 'A':
        if quant <= 5:
            if cartao == 'A':
                total = quant * 5.9
                print(f'Tipo:     Alcatra ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Á vista')
                print('Valor do desconto:     Insento')
                print(f'Valor a pagar:        R${total:.2f}')
            elif cartao == 'S':
                total = quant * 5.9
                novo_total = total * 5 / 100
                print(f'Tipo:      Alcatra ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Cartão Tabajara')
                print('Valor do desconto:     5 %')
                print(f'Valor a pagar:        R${total:.2f}')

        elif quant > 5:
            if cartao == 'N':
                total = quant * 6.8
                print(f'Tipo:      Alcatra ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Á vista')
                print('Valor do desconto:     Insento')
                print(f'Valor a pagar:        R${total:.2f}')
            elif cartao == 'S':
                total = quant * 6.8
                novo_total = total * 5 / 100
                print(f'Tipo:      Alcatra ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Cartão Tabajara')
                print('Valor do desconto:     5 %')
                print(f'Valor a pagar:        R${total:.2f}')

    elif tipo == 'P':
        if quant <= 5:
            if cartao == 'A':
                total = quant * 6.9
                print(f'Tipo:      Picanha ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Á vista')
                print('Valor do desconto:     Insento')
                print(f'Valor a pagar:        R${total:.2f}')
            elif cartao == 'S':
                total = quant * 6.9
                novo_total = total * 5 / 100
                print(f'Tipo:      Picanha ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Cartão Tabajara')
                print('Valor do desconto:     5 %')
                print(f'Valor a pagar:        R${total:.2f}')

        elif quant > 5:
            if cartao == 'N':
                total = quant * 7.8
                print(f'Tipo:      Picanha ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Á vista')
                print('Valor do desconto:     Insento')
                print(f'Valor a pagar:        R${total:.2f}')
            elif cartao == 'S':
                total = quant * 7.8
                novo_total = total * 5 / 100
                print(f'Tipo:      Picanha ----- {quant} Kg')
                print(f'Preço total:          R${total:.2f}')
                print(f'Tipo de pagametno:    Cartão Tabajara')
                print('Valor do desconto:     5 %')
                print(f'Valor a pagar:        R${total:.2f}')

main()
