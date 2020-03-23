#08.Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
#depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
#11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
#ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
#quantidade de horas trabalhadas no mês.
#Desconto do IR:
#o Salário Bruto até R$ 900,00 (inclusive) - isento
#o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
#o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
#o Salário Bruto acima de R$ 2.500,00 - desconto de 20%

def main():
    valor_h = float(input('Qual o seu valor pago por hora:'))
    horas_mensal = int(input('Qual sua quantidade de horas trabalhadas:'))

    print('\n********* FOLHA DE PAGAMENTO *********\n')
    folha_pagamento(valor_h, horas_mensal)
    print('\n**************************************')

def folha_pagamento(valor_h, horas_mensal):
    salario_bruto = valor_h * horas_mensal
    fgts = salario_bruto * 11 / 100
    inss = salario_bruto * 10 / 100

    if salario_bruto <= 900:
        total = fgts + inss
        salario_liquido = salario_bruto - total

        print(f'SALÁRIO BRUTO:       R${salario_bruto:.2f} ')
        print('(-)IR:                 INSENTO')
        print(f'(-)INSS(10%):        R${inss:.2f} ')
        print(f'FGTS(11%):           R${fgts:.2f}')
        print(f'TOTAL DE DESCONTOS:  R${total:.2f}')
        print(f'SALÁRIO LÍQUIDO:     R${salario_liquido:.2f}')

    elif salario_bruto <= 1500:
        ir = salario_bruto * 5 / 100
        total = fgts + inss + ir
        salario_liquido = salario_bruto - total

        print(f'SALÁRIO BRUTO:       R${salario_bruto:.2f} ')
        print(f'(-)IR(5%):           R${ir:.2f}')
        print(f'(-)INSS(10%):        R${inss:.2f} ')
        print(f'FGTS(11%):           R${fgts:.2f}')
        print(f'TOTAL DE DESCONTOS:  R${total:.2f}')
        print(f'SALÁRIO LÍQUIDO:     R${salario_liquido:.2f}')

    elif salario_bruto <= 2500:
        ir = salario_bruto * 10 / 100
        total = fgts + inss + ir
        salario_liquido = salario_bruto - total

        print(f'SALÁRIO BRUTO:       R${salario_bruto:.2f} ')
        print(f'(-)IR(10%):          R${ir:.2f}')
        print(f'(-)INSS(10%):        R${inss:.2f} ')
        print(f'FGTS(11%):           R${fgts:.2f}')
        print(f'TOTAL DE DESCONTOS:  R${total:.2f}')
        print(f'SALÁRIO LÍQUIDO:     R${salario_liquido:.2f}')

    elif salario_bruto > 2500:
        ir = salario_bruto * 20 / 100
        total = fgts + inss + ir
        salario_liquido = salario_bruto - total

        print(f'SALÁRIO BRUTO:       R${salario_bruto:.2f} ')
        print(f'(-)IR(20%):          R${ir:.2f}')
        print(f'(-)INSS(10%):        R${inss:.2f} ')
        print(f'FGTS(11%):           R${fgts:.2f}')
        print(f'TOTAL DE DESCONTOS:  R${total:.2f}')
        print(f'SALÁRIO LÍQUIDO:     R${salario_liquido:.2f}')

main()
