def main():
    
    print(igual())
    
def igual():
    n = int(input('Digite a quantidade de elementos no vetor: '))
    vetor = []
    
    for _ in range(n):
        vetor.append(int(input('Digite um valor a ser adicionado: ')))
    if len(vetor) == 1:
        print('Vetor de tamanho 1')
    
    elif len(vetor) == 2:
        if vetor[0] == vetor[1]:
            return True

    elif len(vetor) >= 3:
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                if vetor[i] == vetor[j]:
                    return True

main()

