def main():
    
    num = int(input('Digite o número de pessoas: '))
    
    cont = 1
    acum = 0
    salario_total = 0
    filhos_total = 0

    while num >= cont:
    
        salario = int(input('Digite o salário da pessoa: '))
        salario_total += salario
        
        if salario <= 1000:
            acum += 1

        filhos = int(input('Digite a quantidade de filhos: '))
        filhos_total += filhos
            
        cont += 1
        

    print('-=' * 30)
    print(f"Média salarial da população: R${salario_total / num:.2f}")
    print(f'Média do número de filhos: {filhos_total / num}')
    print(f'Percentual de pessoas com salário até R$1000.00: {((100 * acum) / num)} %')
    print('-=' * 30)
                


main()
