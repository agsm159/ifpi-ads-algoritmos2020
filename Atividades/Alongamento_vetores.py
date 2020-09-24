def main():

    n = int(input('Digite a quantidade de números desejados: '))
    vetor = [-1] * n
    vetor = lista(n, vetor)

    print('-----------------------------BÁSICO--------------------------------------')
    print('=-' * 30)
    print(f'Quantidade de números pares: {par_and_impar(vetor)[0]} ')
    print(f'Quantidade de números ímpares: {par_and_impar(vetor)[1]}')
    print('=-' * 30)
    print(f'Quantidade de números positivos: {positivo_and_negativo(vetor)[0]}')
    print(f'Quantidade de números negativos: {positivo_and_negativo(vetor)[1]}')
    print('=-' * 30)

    vetor = dobro_and_metade(n, vetor)
    print('-----------------------------EVOLUÇÃO------------------------------------')
    print(f'Quantidade de números pares: {par_and_impar(vetor)[0]} ')
    print(f'Quantidade de números ímpares: {par_and_impar(vetor)[1]}')
    print('=-' * 30)
    print(f'Quantidade de números positivos: {positivo_and_negativo(vetor)[0]} ')
    print(f'Quantidade de números negativos: {positivo_and_negativo(vetor)[1]}')
    print('=-' * 30)
    print(f'O valor da média após as transformações é: {media(n, vetor)}')

    
def lista(n, v):

    for i in range(0, n, 1):
        v[i] = int(input(f'Digite o {i + 1}º número: '))
    
    return v

def par_and_impar(v):
    par = 0
    impar = 0

    for i in range(0, len(v), 1):
        
        if v[i] % 2 == 0:
            par += 1
        else:
            impar += 1
    
    par_impar = [0] * 2
    par_impar[0] = par
    par_impar[1] =  impar

    return par_impar

def positivo_and_negativo(v):
    positivo = 0
    negativo = 0

    for i in range(0, len(v), 1):
        
        if v[i] >= 0:
            positivo += 1
        else:
            negativo += 1

    positivo_negativo = [0] * 2
    positivo_negativo[0] = positivo
    positivo_negativo[1] = negativo

    return positivo_negativo

def dobro_and_metade(n, v):

    for i in range(0, n, 1):
        
        if v[i] >= 0:
            v[i] = v[i] * 2
        else:
            v[i] = v[i] / 2
    
    return v

def media(n, v):
    soma = 0

    for i in range(0, n, 1):
        
        soma += v[i]
    media = soma / n

    return media

main()
