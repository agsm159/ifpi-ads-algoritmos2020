#07.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
#contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
#salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#o salários até R$ 280,00 (incluindo) : aumento de 20%
#o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#· o salário antes do reajuste;
#· o percentual de aumento aplicado;
#· o valor do aumento;
#· o novo salário, após o aumento.

def main():
    salario = float(input('Quantia do salário: R$'))

    print('\n*******REAJUSTE SALÁRIAL*******\n')
    print(aumento_salarial(salario))
    print('\n*******************************')

def aumento_salarial(salario):

    if salario <= 280:
        aumento_sal = salario * 20 / 100
        print(f'\nSalário antes do reajuste: R${salario:.2f}')
        print('Percentual de aumento: 20%')
        print(f'Quantia do aumento: R${aumento_sal:.2f}')
        print(f'Salário após o reajuste: R${salario + aumento_sal:.2f}')

    elif salario > 280 and salario <= 700:
        aumento_sal = salario * 15 / 100
        print(f'\nSalário antes do reajuste: R${salario:.2f}')
        print('Percentual de aumento: 15%')
        print(f'Quantia do aumento: R${aumento_sal:.2f}')
        print(f'Salário após o reajuste: R${salario + aumento_sal:.2f}')

    elif salario > 700 and salario <= 1500:
        aumento_sal = salario * 10 / 100
        print(f'\nSalário antes do reajuste: R${salario:.2f}')
        print('Percentual de aumento: 10%')
        print(f'Quantia do aumento: R${aumento_sal:.2f}')
        print(f'Salário após o reajuste: R${salario + aumento_sal:.2f}')

    elif salario > 1500:
        aumento_sal = salario * 5 / 100
        print(f'\nSalário antes do reajuste: R${salario:.2f}')
        print('Percentual de aumento: 5%')
        print(f'Quantia do aumento: R${aumento_sal:.2f}')
        print(f'Salário após o reajuste: R${salario + aumento_sal:.2f}')

main()
