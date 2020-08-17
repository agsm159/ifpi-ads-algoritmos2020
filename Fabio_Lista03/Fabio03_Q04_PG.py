def main():

    valor_inicial = int(input('Digite um inicio da progressão: '))
    limite = int(input('Digite o limite da progressão: '))
    razao = int(input('Digite a razão: '))

    cont = 1
    v = 0

    while limite >= v:
        v = valor_inicial * razao ** (cont - 1)

        if limite > v:
            print(v)
        
        cont = cont + 1

main()
