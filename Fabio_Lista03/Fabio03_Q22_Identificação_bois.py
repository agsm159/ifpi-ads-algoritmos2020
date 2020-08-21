def main():
    
    num = int(input('Digite o número de bois: '))
    cont = 1
    num_ident = 0
    peso = 0
    num_maior = 1
    peso_maior = 0
    num_menor = 1
    peso_menor = 1000

    while cont <= num:

        num_ident = int(input('Digite o número do boi: '))
        peso = int(input('Digite o peso do boi(Kg): '))

        if peso > peso_maior:
            num_maior = num_ident
            peso_maior = peso
        
        if peso < peso_menor:
            num_menor = num_ident
            peso_menor = peso
        
        cont += 1
    
    print(f'O boi mais pesado, possui número de identificação {num_maior} e peso {peso_maior} Kg.')
    print(f'O boi mais leve possui número de identificação {num_menor} e peso {peso_menor} Kg.')



main()
