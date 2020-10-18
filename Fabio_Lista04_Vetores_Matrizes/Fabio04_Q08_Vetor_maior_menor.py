def main():
    lista = []
    maior = [0, 0]
    menor = [1000000000000, 0]
    
    n = int(input('Digite a quantidade de valores da lista: '))
    
    for i in range(0, n, 1):

        lista.append(int(input('Digite o(s) elemento(s) da lista: ')))
        if lista[i] > lista[i - 1]:
            maior[0] = lista[i]
            maior[1] = i
        
        if lista[i] < menor[0]:
            menor[0] = lista[i]
            menor[1] = i

   
    print(maior[0], menor[1])
    print('-+' * 30)
    print(menor[0], menor[1])

main()
