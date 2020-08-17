def main():
    import math
    n = int(input('Digite a quantidade de números: '))
    
    cont = 1
    maior = 0
    valor_atual = 0
    valor_anterior = 0

    while cont <= n:

        valor_atual = int(input('Digite um valor: '))
        valor_atual = (math.sqrt(valor_atual))
        if valor_atual > valor_anterior:
            maior = valor_atual
            valor_anterior = valor_atual
            maior = maior ** 2
        cont = cont + 1
        
    print(f'O maior quadrado menor é : {maior}')
    

main()
