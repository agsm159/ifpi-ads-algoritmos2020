def main():
    
    matriz = formar_matriz()
    imp_matriz(matriz,'Matriz Criada:\n')
    matriz = preencher_matriz(matriz)
    imp_matriz(matriz,'Matriz preenchida:\n')
    print(simetrica(matriz))

def formar_matriz():
    ordem = int(input('Digite o valor da ordem: '))
    matriz = []
    
    for i in range(ordem):
        matriz.append([i] * ordem)

    return matriz

def preencher_matriz(matriz):
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input('Digite o valor para: '))

    return matriz

def simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != j:
                if matriz[i][j] != matriz[j][i]:
                    return 'Não simetrica'
    
    return 'Simetrica'

def imp_matriz(matriz, texto):
    print('-' * 30)
    for i in range(len(matriz)):
        if i != 0:    
            print('',matriz[i])
        else:
            print(texto,matriz[i])
    print('-' * 30)

main()
