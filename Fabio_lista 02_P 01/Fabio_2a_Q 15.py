#15.Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
#Escreva na tela qual dos professores tem salário total maior.

def main():
    hora_prof1 = int(input('Digite a quantidades de horas aula dada pelo primeiro professor:'))
    hora_prof2 = int(input('Digite a quantidades de horas aula dada pelo segundo professor:'))

    valor_prof1 = int(input('Digite valor da hora aula do primeiro professor: R$'))
    valor_prof2 = int(input('Digite valor da hora aula do segundo professor: R$'))

    salário_prof1 = hora_prof1 * valor_prof1
    salário_prof2 = hora_prof2 * valor_prof2

    maior_salário(salário_prof1, salário_prof2)

def maior_salário(salário_prof1, salário_prof2):
    if salário_prof1 > salário_prof2:
        print(f'O salário do professor 1 é maior que do professor 2')

    else:
        print(f'O salário do professor 1 é menor que do professor 2')

main()
