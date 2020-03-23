#04.Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
#o "Aprovado", se a média alcançada for maior ou igual a sete;
#o "Reprovado", se a média for menor do que sete;
#o "Aprovado com Distinção", se a média for igual a dez.

def main():
    nota_1 = float(input('Quanto foi tirado na 1º nota:'))
    nota_2 = float(input('Quanto foi tirado na 2º nota:'))

    print(verificação(nota_1, nota_2))

def verificação(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2

    if media >= 7:
        print('\nAluno APROVADO!')

    elif media == 10:
        print('\nAluno APROVADO COM DISTINÇÃO!!!')

    else:
        print('\nAluno REPROVADO!')

main()
