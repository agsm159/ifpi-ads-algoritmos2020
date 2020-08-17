def main():
    
    n = int(input('Digite a quantidade de números: '))
    
    cont = 1
    maior = 0
    valor_atual = 0
    valor_anterior = 0

    while cont <= n:

        valor_atual = int(input('Digite um valor: '))
        if valor_atual > valor_anterior:
            maior = valor_atual
            valor_anterior = valor_atual
        cont = cont + 1
        
    print(f'O maior valor é: {maior}')
    

main()
