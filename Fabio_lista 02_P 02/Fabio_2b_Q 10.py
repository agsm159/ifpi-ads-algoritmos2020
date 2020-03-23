#10.Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
#sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento Conceito
#Entre 9.0 e 10.0 A
#Entre 7.5 e 9.0 B
#Entre 6.0 e 7.5 C
#Entre 4.0 e 6.0 D
#Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
#“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def main():
    nota_1 = float(input('Quanto foi a 1º nota?\n'))
    nota_2 = float(input('Quanto foi a 2º nota?\n'))

    print('\n******* CODIÇÃO NO SEMESTRE *******\n')
    aprov_reprov(nota_1, nota_2)
    print('\n***********************************')

def aprov_reprov(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2

    if media >= 9 and media <= 10:
        print(f'1º Nota:                 {nota_1}')
        print(f'2º Nota:                 {nota_2}')
        print(f'Sua média foi:           {media:.1f}')
        print('Conceito correspondente:  A')
        print('Condição do aluno:        APROVADO ')

    elif media >= 7.5 and media < 9:
        print(f'1º Nota:                 {nota_1}')
        print(f'2º Nota:                 {nota_2}')
        print(f'Sua média foi:           {media:.1f}')
        print('Conceito correspondente:  B')
        print('Condição do aluno:        APROVADO ')

    elif media >= 6 and media < 7.5:
        print(f'1º Nota:                 {nota_1}')
        print(f'2º Nota:                 {nota_2}')
        print(f'Sua média foi:           {media:.1f}')
        print('Conceito correspondente:  C')
        print('Condição do aluno:        APROVADO ')

    elif media >= 4 and media < 6:
        print(f'1º Nota:                 {nota_1}')
        print(f'2º Nota:                 {nota_2}')
        print(f'Sua média foi:           {media:.1f}')
        print('Conceito correspondente:  D')
        print('Condição do aluno:        REPROVADO ')

    elif media < 4:
        print(f'1º Nota:                 {nota_1}')
        print(f'2º Nota:                 {nota_2}')
        print(f'Sua média foi:           {media:.1f}')
        print('Conceito correspondente:  E')
        print('Condição do aluno:        REPROVADO ')

main()
