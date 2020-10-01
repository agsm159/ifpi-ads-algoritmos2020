def main():
    menu = '** Brincando com Listas **'
    menu += '\n 1 - Inserir Novos Valores'
    menu += '\n 2 - Mostrar Valor em Determinada posição'
    menu += '\n 3 - mostrar Todos os Valores da Lista'
    menu += '\n 4 - Remover do Ínicio, Final ou Posição Específica'
    menu += '\n 5 - inserir Valor na Posição Específica'
    menu += '\n 6 - Quantidade de Pares, Impares, Primos, Positivos, Negativos e Nulos'
    menu += '\n 7 - Média dos Valores do Vetor'
    menu += '\n 8 - ocorrência De Um Determinado Dado e seu Valor'
    menu += '\n 9 - Dobrar Todos os Valores'
    menu += '\n 10 - Múltiplos de Determinado Valor'
    menu += '\n 11 - Apagar Todos os Valores'
    menu += '\n 0 - Sair '
    menu += "\n Obs: Se for a primeira vez executando, utilize a opção 1 primeiro para inserir os valores..."
    menu += '\n\n Opção >>> '

    lista= []

    while True:  
            opcao = int(input(menu))

            if opcao == 1:
                inserir_valores(lista)
            elif opcao == 2:
                mostra_valor(lista)
            elif opcao == 3:
                mostrar_todos(lista)
            elif opcao == 4:
                remove(lista)
            elif opcao == 5:
                inserir(lista)
            elif opcao == 6:
                contagem(lista)
            elif opcao == 7:
                media_vetor(lista)
            elif opcao == 8:
                valores_repetidos(lista)
            elif opcao == 9:
                dobro(lista)
            elif opcao == 10:
                multiplo(lista)
            elif opcao == 11:
                remover(lista)
            elif opcao == 0:  
                break
            else:
                print('Opção Inválida')

#-------------- OPÇÃO 01 --------------
def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir?'))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    input('<enter> to continue...')

#-------------- OPÇÃO 02 --------------
def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(lista[posicao])

    input('<enter> to continue...')

#-------------- OPÇÃO 03 --------------
def mostrar_todos(lista):
    print(lista)

    input('<enter> to continue...')

#--------------- OPÇÃO 04 -------------
def remove(lista):
    menu_remove = '** Escolha **'
    menu_remove += '\n 0 - Sair'
    menu_remove += '\n 1 - Remover do Ínicio'
    menu_remove += '\n 2 - Remover do Final'
    menu_remove += '\n 3 - Remover em Índice N'
    menu_remove += '\n\n Opção >>> '

    opcao_remove = int(input(menu_remove))

    if opcao_remove == 1:
        lista.pop(0)
    elif opcao_remove == 2:
        lista.pop(len(lista) - 1)
    elif opcao_remove == 3:
        indice = int(input('Digite o índice que deseja remover: '))
        lista.pop(indice)
    elif opcao_remove == 0:
        input('<enter> to continue...')
    else:
        print('Opção ínvalida')

#--------------- OPÇÃO 05 -------------
def inserir(lista):
    indice = int(input('Digite o índice que deseja adicionar o valor: '))
    lista[indice] = int(input(f'Digite o valor que deseja inserir no índice: {indice}'))
    input('<enter> to continue...')

#-------------- OPÇÃO 06 --------------
def contagem(lista):
    menu_contagem = '** Escolha **'
    menu_contagem += '\n 0 - Sair'
    menu_contagem += '\n 1 - Pares'
    menu_contagem += '\n 2 - Impares'
    menu_contagem += '\n 3 - Primos'
    menu_contagem += '\n 4 - Positivo'
    menu_contagem += '\n 5 - Negativo'
    menu_contagem += '\n 6 - Nulo'
    menu_contagem+= '\n\n Opção >>> '

    menu_numero = int(input(menu_contagem))

    if menu_numero == 1:
        pares = 0
        for i in lista:
            if i % 2 == 0:
                pares += 1
        print(f'Quantidade de pares: {pares}')
    elif menu_numero == 2:
        impares = 0
        for i in lista:
            if i % 2 != 0:
                impares += 1
        print(f'Quantidade de impares: {impares}')
    elif menu_numero == 3:
        print(f'Quantidade de primos: {e_primo(lista)}')
    elif menu_numero == 4:
        positivos = 0
        for i in lista:
            if i >= 0:
                positivos += 1
        print(f'Quantidade de positivos: {positivos}')
    elif menu_numero == 5:
        negativo = 0
        for i in lista:
            if i < 0:
                negativo += 1
        print(f'Quantidade de negativos: {negativo}')   
    elif menu_numero == 6:
        nulo = 0
        for i in lista:
            if i == 0:
                nulo += 1

        print(f'Quantidade de nulos: {nulo}')
    elif menu_numero == 0:
        input('<enter> to continue...')
    else:
        print('Opção Invalida!')

def e_primo(lista):
    primos = int(0)
    for i in lista:
        primos += primo(i)
    return primos

def primo(n):
    acum = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            acum += 1
        
    if acum == 2:
        return int(1)
    else:
        return int(0)

#--------------- OPÇÃO 07 ---------------
def media_vetor(lista):
    soma = 0
    
    for i in lista:
        soma += i
    media = soma / len(lista)

    print(f'A média dos valores da lista é: {media}')
    input('<enter> to continue...')

#--------------- OPÇÃO 08 ---------------
def valores_repetidos(lista):
    ocorrencia = 0
    n = int(input('Digite o valor do dado que deseja verificar o numeros de repetiçôes: '))
    for i in lista:
        if i == n:
            ocorrencia += 1

    print(f'O número de repetições do número é: {ocorrencia}')
    input('<enter> to continue...')

#---------------- OPÇÃO 09 --------------
def dobro(lista):
    j = 0
    for i in lista:
        lista[j] = i * 2
        j += 1

    print(f'O dobro da lista é: {lista}')
    input('<enter> to continue...')

#--------------- OPÇÃO 10 ---------------
def multiplo(lista):
    n = int(input('Digite o valor que deseja verificar o seus multiplos: '))
    lista2 = []
    j = 0
    for i in lista:
        if i % n == 0:
            lista2.append(i * 2)
        else:
            lista.appende(i)
        j += 1

    print(f'Anterior: {lista}')
    print(f'O dobro dos multiplos de {n}, são {lista2} ')
    input('<enter> to continue...')

#--------------- OPÇÃO 11 ---------------
def remover(lista):
    lista.clear()
        
    print('Os valores da lista foram removidos!')
    input('<enter> to continue...')


main()