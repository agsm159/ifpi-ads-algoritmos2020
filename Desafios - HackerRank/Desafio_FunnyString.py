def main():
    mensagem = input("Digite a mensagem desejada: ")
    
    print(funnystring(mensagem, reverse(mensagem)))

def funnystring(m, r):
    
    if mensagem_1(m) == mensagem_2(r):
        return 'Funny :)'
    else:
        return 'Not Funny :('


def mensagem_1(m):
    string = ''
    valor_anterior = 0
    i = 1
    for a in m:
        valor_atual = ord(a)
        if i > 1:
            string += str(valor_atual - valor_anterior)
        valor_anterior = valor_atual
        i += 1
    
    return string

def mensagem_2(r):
    mensagem_reverse = ''
    valor_anterior = 0
    j = 1
    for b in r:
        valor_atual = ord(b)
        if j > 1:
            mensagem_reverse += str(valor_anterior - valor_atual)
        valor_anterior = valor_atual
        j += 1
    
    return mensagem_reverse

def reverse(m):
    retorno = ''
    for i in range(len(m)-1, -1, -1):
        retorno += m[i]

    return retorno
    
main()
