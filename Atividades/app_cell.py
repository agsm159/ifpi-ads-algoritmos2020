import os
import json

def main():
    
    celulares = inicializar('celulares.bd')
    menu = tela_principal()
    opcao = int(input(menu))

    while opcao != 0:

        if opcao == 1:
            print('Criando novo celular.')
            celular = criar_celular()
            celulares.append(celular)
            print('Celular cadastrado com sucesso!')

        elif opcao == 2:
            listar_celular(celulares)

        elif opcao == 3:
            buscar(celulares)
        input('press <enter> to continue...')
        opcao = int(input(menu))
    # ---- Finalizar ----
    finalizar('celulares.bd', celulares)

def tela_principal():
    
    menu = str('*** App Cell ***\n')
    menu += '1 - Novo celular\n'
    menu += '2 - listar  celulares\n'
    menu += '3 - Buscar celulares\n'
    menu += '0 - sair\n'
    menu += '\nOpçao desejada >>> '

    return menu

def inicializar(nome_arquivo):
    charged_cells = []

    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        charged_cells = json.loads(dados)

    return charged_cells

def finalizar(nome_arquivo, celulares):
    
    dados = json.dumps(celulares)
    
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()

def criar_celular():
    
    print('----- Novo celular -----')

    # ------ Dados do celular ------
    nome = input('Nome: ')
    marca = input('Marca: ')
    tela = input('Tela ":')
    valor = float(input('Valor R$: '))
    cam_frontal = input('Camêra frontal[S/N]: ')

    # ------ Montar celular ------
    celular = {}
    celular['nome'] = nome
    celular['marca'] = marca
    celular['tela'] = tela
    celular['valor'] = valor
    celular['cam_frontal'] = cam_frontal

    return celular

def listar_celular(celulares):
    quant = len(celulares)
    print(f'Listando {quant} celulares.')

    for celular in celulares:
        print("________________________________________")
        print('Nome:', celular['nome'])
        print('marca:', celular['marca'])
        print('valor:', celular['valor'])
        print('tela:', celular['tela'])
        print('frontal:', celular['cam_frontal'])
        print("________________________________________")


def buscar(celulares):
    string = input('Digite o nome ou marca do celular: ')
    i = 0

    for celular in celulares:
        if string in celular['nome']:
            print('-=-' * 15)
            print(f'Codigo: 00{i}')
            print('Nome:', celular['nome'])
            print(f'Marca:', celular['marca'])
            print('-=-' * 15)
        elif string in celular['marca']:
            print('-=-' * 15)
            print(f'Codigo: 00{i}')
            print(f'Nome:', celular['nome'])
            print(f'Marca:', celular['marca'])
            print('-=-' * 15)
        i += 1

    continuar = input('Deseja selecionar algum dos celulares: [S/N]: ')
    continuar = continuar.upper()

    if continuar == 'S':
        selecionado = int(input('Digite o código do celular listado que deseja selecionar: '))
        selecionar_celular(celulares, selecionado)


def selecionar_celular(celulares, selecionado):
    menu = str('*********** Seleção ***********\n')
    menu += '1 - Exibir detalhes do celular\n'
    menu += '2 - Remover celular\n'
    menu += '3 - Editar celular\n'
    menu += '4 - Duplicar celular\n'
    menu += '0 - sair\n'
    opçao = int(input(menu))

    if opçao == 1:
        
        print('-=-' * 20)
        print('Nome:', celulares[selecionado]['nome'])
        print('Marca:', celulares[selecionado]['marca'])
        print('Tela:', celulares[selecionado]['tela'])
        print('Valor:', celulares[selecionado]['valor'])
        
    elif opçao == 2:
        
        del celulares[selecionado]
        print('Celular deletado!!!')

    elif opçao == 3:
        
        menu_ediçao = str('***** Edição *****\n')
        menu_ediçao += '1 - Editar nome\n'
        menu_ediçao += '2 - Editar marca\n'
        menu_ediçao += '3 - Editar tela\n'
        menu_ediçao += '4 - Editar valor\n'
        menu_ediçao += '5 - Editar câmera\n'
        menu_ediçao += '6 - Editar tudo\n'
        opçao_ediçao = int(input(menu_ediçao))

        if opçao_ediçao == 1 or opçao_ediçao == 6:
            celulares[selecionado]['nome'] = input('Novo nome para o celular: ')
        if opçao_ediçao == 2 or opçao_ediçao == 6:
            celulares[selecionado]['marca'] = input('Nova marca para o celular: ')
        if opçao_ediçao == 3 or opçao_ediçao == 6:
            celulares[selecionado]['tela'] = input('Novo temanho de tela para o celular: ')
        if opçao_ediçao == 4 or opçao_ediçao == 6:
            celulares[selecionado]['valor'] = float(input('Novo preço para o celular: '))
        if opçao_ediçao == 5 or opçao_ediçao == 6:
            celulares[selecionado]['frontal'] = input('O celular possui câmera frontal [S/N]: ')

    elif opçao == 4:
        celulares.append(celulares[selecionado])


main()
