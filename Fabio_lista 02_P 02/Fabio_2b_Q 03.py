#03.Leia uma letra e verifique se a letra digitada é vogal ou consoante.

def main():
    letra = input('Digite uma letra:')

    print( vogal_consoante(letra) )

def vogal_consoante(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(f'\nA letra {letra} é uma vogal')

    else:
        print(f'\nA letra {letra} é uma consoante.')

main()
