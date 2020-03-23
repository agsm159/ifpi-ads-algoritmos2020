#15.Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#           Até 5 Kg        Acima de 5 Kg
#Morango R$ 2,50 por Kg    R$ 2,20 por Kg
#Maçã    R$ 1,80 por Kg    R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
#ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
#morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def main():
    print('************** Frutaria *****************************\n')
    print('Tabela de preços:  Até 5 kg          Acima de 5 kg')
    print('Morango:        R$ 2.50 por kg     R$ 2.20 por kg')
    print('Maçã:           R$ 1.80 por kg     R$ 1.50 por kg')
    print('\n*****************************************************\n')

    morango_kg = int(input('Quantos quilos de morango você deseja:'))
    maça_kg = int(input('Quantos quilos de maçã você deseja:'))

    pagamento(morango_kg, maça_kg)

def pagamento(morango_kg,maça_kg):
    total_kg = morango_kg + maça_kg
    desconto = total_kg * 10 / 100

    if morango_kg <= 5 and maça_kg <= 5:
        if total_kg < 8:
            valor_mor = morango_kg * 2.5
            valor_maça = maça_kg * 1.8
            total = valor_mor + valor_maça
            print(f'\nValor a ser pago: R${total:.2f}')

        elif total_kg >= 8:
            valor_mor = morango_kg * 2.5
            valor_maça = maça_kg * 1.8
            total = valor_mor + valor_maça
            novo_total = total - desconto
            print(f'\nValor a ser pago: R${novo_total:.2f}')

    elif morango_kg <= 5 and maça_kg > 5:
        if total_kg < 8:
            valor_mor = morango_kg * 2.5
            valor_maça = maça_kg * 1.5
            total = valor_mor + valor_maça
            print(f'\nValor a ser pago: R${total:.2f}')

        elif total_kg >= 8:
            valor_mor = morango_kg * 2.5
            valor_maça = maça_kg * 1.5
            total = valor_mor + valor_maça
            novo_total = total - desconto
            print(f'\nValor a ser pago: R${novo_total:.2f}')

    elif morango_kg > 5 and maça_kg <= 5:
        if total_kg < 8:
            valor_mor = morango_kg * 2.2
            valor_maça = maça_kg * 1.8
            total = valor_mor + valor_maça
            print(f'\nValor a ser pago: R${total:.2f}')

        elif total_kg >= 8:
            valor_mor = morango_kg * 2.2
            valor_maça = maça_kg * 1.8
            total = valor_mor + valor_maça
            novo_total = total - desconto
            print(f'\nValor a ser pago: R${novo_total:.2f}')

    elif morango_kg > 5 and maça_kg > 5:
        valor_mor = morango_kg * 2.2
        valor_maça = maça_kg * 1.5
        total = valor_mor + valor_maça
        novo_total = total - desconto
        print(f'\nValor a ser pago: R${novo_total:.2f}')

main()
