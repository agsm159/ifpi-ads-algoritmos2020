#13.Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a) "Telefonou para a vítima ?"
#b) "Esteve no local do crime ?"
#c) "Mora perto da vítima ?"
#d) "Devia para a vítima ?"
#e) "Já trabalhou com a vítima ?"
#O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
#responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
#"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def main():
    print('Responda as seguintes perguntas com "S" (para Sim) ou "N" (para Não).\n')
    p1 = str(input('Você telefonou para a vítima?\n'))
    p2 = str(input('Você esteve no local do crime?\n'))
    p3 = str(input('Você mora perto da vítima?\n'))
    p4 = str(input('Você devia para a vítima?\n'))
    p5 = str(input('Você já trabalhou com vítima?\n'))

    classificação(p1, p2, p3, p4, p5)

def classificação(p1, p2, p3, p4, p5):
    if p1 and p2 and p3 and p4 and p5 == 'S':
        print('\nVocê é o assasino!!!')

    elif p1 and p2 == 'S' or p1 and p3 == 'S' or p1 and p4 == 'S' or p1 and p5 == 'S':
        print('\nVocê é um suspeito!')

    elif p2 and p3 == 'S' or p2 and p4 == 'S' or p2 and p5 == 'S':
        print('\nVocê é um suspeito!')

    elif p3 and p4 == 'S' or p3 and p5 == 'S' or p4 and p5 == 'S':
        print('\nVocê é um suspeito!')

    elif p1 and p2 and p3 and p4 and p5 == 'N':
        print('\nVocê é inocente')

    else:
        print('\nVocê é um cúmplice!!')

main()
