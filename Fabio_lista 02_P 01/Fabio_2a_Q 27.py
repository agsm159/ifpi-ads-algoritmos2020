#27.Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
#nascimento e a data (dia, mês e ano) atual.

def main():
    print('Imforme a data atual:\n')
    dia_atual = int(input('Digite o dia atual:'))
    mes_atual = int(input('Digite o mês atual:'))
    ano_atual = int(input('Digite o ano atual:'))

    print('\nImforme sua data de nascimento:\n')
    dia_nasc = int(input('Qual o seu dia de nascimento:'))
    mes_nasc = int(input('Qual o seu mês de nascimento:'))
    ano_nasc = int(input('Qual o seu ano de nascimento:'))

    idade_atual = descobrir_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)
    print(idade_atual)

def descobrir_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    total_dias_atual = (ano_atual * 365) + (mes_atual * 30) + dia_atual
    total_dias_nasc = (ano_nasc * 365) + (mes_atual * 30) + dia_nasc
    total_idade_em_dias = total_dias_atual - total_dias_nasc

    anos = (total_idade_em_dias // 365)
    meses = (total_idade_em_dias % 365) // 30
    dias =(total_idade_em_dias % 365) % 30

    if total_dias_atual > total_dias_nasc:
        print(f'\nA sua idade é de {anos} anos, {meses} meses e {dias} dias.')

    else:
        print('\nParabéns!!! Você nasceu hoje!!!!')

main()
