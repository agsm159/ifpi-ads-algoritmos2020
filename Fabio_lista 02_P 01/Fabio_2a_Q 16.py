#16.Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
#ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
#final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
#escreva “Reprovado”.

def main():
    nota_1 = float(input('Digite a primeira nota:'))
    nota_2 = float(input('Digite a segunda nota:'))

    media_sem = (nota_1 + nota_2) / 2

    media(nota_1, nota_2, media_sem )

def media(nota_1, nota_2, media_sem):
    if media_sem >= 7:
        print('O aluno está aprovado!')

    elif media_sem < 7:
        nota_final = float(input('Digite a nota final:'))
        media_final = (media_sem + nota_final) / 2

        if media_final >= 5:
            print('O aluno esta aprovado!')

        else:
            print('O aluno esta reprovado!')

main()
