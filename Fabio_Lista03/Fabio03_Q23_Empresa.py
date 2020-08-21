def main():
    
    num_func = int(input('Digite o número de funcionários: '))
    
    cont = 1
    salario = 0

    while num_func <= cont:
    
        func = int(input('Digite o código do funcionário: '))
        horas = int(input('Digite a quantidade de horas de trabalho: '))
        dependentes = int(input('Digite a quantidade de dependentes do funcionário: '))

        salario = (horas * 12) + (dependentes * 40)
        IR = salario * 0.05
        INSS = salario * 0.085
        salario_liquido = float(salario - IR - INSS)

        print('-=' * 30)
        print(f"Funcionário Nº: {func}\n Horas trabalhadas: {horas} h \n Nº de dependentes: {dependentes}")
        print(f'Salário bruto: R${salario} e Salário liquído: R${salario_liquido} ')
        print(f'Valores descontados: INSS: R${INSS} e  IR: R${IR}')
        print('-=' * 30)
        
        cont += 1


main()
