def main():
    
    matriz = formar_matriz()
    imp_matriz(matriz,'Matriz Criada:\n')
    soma = preencher_matriz(matriz)
    linha_maior_soma(soma)
    linha_menor_soma(soma)


def formar_matriz():
    ordem = int(input('Digite o valor da ordem: '))
    matriz = []
    
    for i in range(ordem):
        matriz.append([i] * ordem)

    return matriz

def preencher_matriz(matriz):
    soma = [0] * len(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input('Digite o valor para: '))
            soma[i] += matriz[i][j]
    imp_matriz(matriz, 'Matriz preenchida:\n')
    
    return soma

def linha_maior_soma(somas):
    maior = somas[0]
    linha_maior = 1
    for i in range(1, len(somas)):
            if maior < somas[i]:
                linha_maior = i + 1
    
    print("Maior:", linha_maior)

def linha_menor_soma(somas):
    menor = somas[0]
    linha_menor = 1
    for i in range(1, len(somas)):
            if menor > somas[i]:
                linha_menor = i + 1
    
    print("Menor:", linha_menor)


def imp_matriz(matriz, texto):
    print('-' * 30)
    for i in range(len(matriz)):
        if i != 0:    
            print('',matriz[i])
        else:
            print(texto,matriz[i])
    print('-' * 30)

main()
