def main():

    mensagem = str(input('Digite a mensagem que sera enviada: '))

    print(f'Houveram {mars_exploration(mensagem)} letras alteradas durante a transmissão da mensagem.')

def mars_exploration(s):
    i = 1
    cont = 0
    for c in s:
        l = ord(c)
        if i > 3:
            i = 1
        elif (i % 2 == 0) and (l == 79 or l == 111):
            cont += 0
        
        elif (i % 2 != 0) and (l == 83 or l == 115):
            cont += 0
        
        else:
            cont += 1
        i += 1

    return cont

main()
