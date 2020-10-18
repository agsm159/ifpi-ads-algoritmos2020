def main():
    
    matriz = formar_matriz()
    imp_matriz(matriz,'Matriz Criada:\n')
    matriz = preencher_matriz(matriz)
    imp_matriz(matriz,'Matriz preenchida:\n')
    soma_principal = soma_diagonal_principal(matriz)
    soma_secundaria = soma_diagonal_secundaria(matriz)

    print(f'Soma da diagonal principal: {soma_principal}, Soma diagonal secundaria: {soma_secundaria}')

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

def soma_diagonal_principal(matriz):
    soma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                soma += matriz[i][j]
    return soma

def soma_diagonal_secundaria(matriz):
    soma = 0

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(i + j) == (len(matriz) - 1):
                soma += matriz[i][j]
    return soma

def imp_matriz(matriz, texto):
    print('-' * 30)
    for i in range(len(matriz)):
        if i != 0:    
            print('',matriz[i])
        else:
            print(texto,matriz[i])
    print('-' * 30)

main()
