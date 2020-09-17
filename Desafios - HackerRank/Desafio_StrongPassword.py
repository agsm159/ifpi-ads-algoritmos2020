def main():

    _ = int(input('Quantos caracteres a senha possui: '))
    senha = input('Digite a senha para cadastro: ')
    print(senha_forte(senha))

def senha_forte(s):
    if six_words(s):
        condiçao = numeros(s) + letra_maiuscula(s) + letra_minuscula(s) + simbolo(s)
        if condiçao == 4:
            return 'Senha Válida'
        else:
            resultado = 4 - condiçao
            return resultado

    else:
        resultado = 6 - len(s)
        return resultado
            
def six_words(s):
    if len(s) >= 6:
        return True
    else:
        return False

def numeros(s):
    cont = 0
    for c in s:
        c = ord(c)
        if (c >= 48) and (c <= 57):
            cont = 1
    return cont

def letra_maiuscula(s):
    cont = 0
    for c in s:
        c = ord(c)
        if (c >= 65) and (c <= 90):
            cont = 1
    return cont

def letra_minuscula(s):
    cont = 0
    for c in s:   
        c = ord(c)
        if (c >= 97) and (c <= 122):
            cont = 1
    return cont

def simbolo(s):
    cont = 0
    special_characters = "!@#$%^&*()-+"
    for c in s:
        for n in special_characters:
            if n == c:
                cont = 1

    return cont

main()
