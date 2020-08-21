def main():

    num = int(input('Digite a quantidade de eleitores: '))

    cont = 1
    cand_01 = 0
    cand_02 = 0
    cand_03 = 0
    nulo = 0
    branco = 0

    while cont <= num:

        voto = int(input('Digite o número do candidato que deseja votar: '))
        if voto == 1:
            cand_01 += 1
        
        elif voto == 2:
            cand_02 += 1
        
        elif voto == 3:
            cand_03 += 1

        elif voto == 9:
            nulo += 1
        
        elif voto == 0:
            branco += 1

        else:
            print('Voto inválido! Tente novamente!')

        cont += 1

    if cand_01 > cand_02 and cand_01 > cand_03 and cand_01 != cand_02 and cand_01 != cand_03:
        print(f'\nO candidato 1, foi eleito com um total de {cand_01} votos.')

    elif cand_02 > cand_01 and cand_02 > cand_03 and cand_02 != cand_01 and cand_02 != cand_03:
        print(f'\nO candidato 2, foi eleito com um total de {cand_02} votos.')

    elif cand_03 > cand_01 and cand_03 > cand_02 and cand_03 != cand_01 and cand_03 != cand_02:
        print(f'\nO candidato 3, foi eleito com um total de {cand_03} votos.')
    

    print('-=' * 20)
    print(f'Votos do candidato 1: {cand_01}')
    print(f'Votos do candidato 2: {cand_02}')
    print(f'Votos do candidato 3: {cand_03}')
    print(f'Votos em branco: {branco}')
    print(f'Votos nulo: {nulo}')
    print('-=' * 20)


main()
