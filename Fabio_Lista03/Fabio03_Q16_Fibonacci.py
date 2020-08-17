def main():

    n = int(input('Digite a quantidade de valores da sequência: '))

    termo_anterior = 0
    termo_atual = 1
    cont = 1

    while n >= cont:
        print(termo_atual, end = " ")

        s = termo_atual
        termo_atual = termo_atual + termo_anterior
        termo_anterior = s

        cont = cont + 1

main()
