def main():
    
    mensagem = input("Digite a mensagem desejada: ")
    print(sherlock(mensagem))

def sherlock(m):
    cont = 0
    
    for i in range(0, len(m), 1):
        for j in range (i+1, len(m), 1):
            if anagramas(m)[i] == anagramas(m)[j]:
                cont += 1
 
    for i in range(0, len(m)-1, 1):
        for j in range (i+1, len(m)-1, 1):
            if anagramas_duplos(m)[i] == anagramas_duplos(m)[j]:
               cont += 1

    for i in range(0, len(m)-2, 1):
        for j in range (i+1, len(m)-2, 1):
            if anagramas_triplos(m)[i] == anagramas_triplos(m)[j]:
               cont += 1
    
    return cont

def anagramas(m):
    anagramas = []
    for i in m:
        anagramas.append(i)
    
    return anagramas

def anagramas_duplos(m):
    anagramas_duplos = []
    for i in range(0, len(m)-1, 1):
        anagramas_duplos.append(ord(m[i])+ord(m[i+1]))
    
    return anagramas_duplos

def anagramas_triplos(m):
    anagramas_triplos = []
    for i in range(0, len(m)-2, 1):
        anagramas_triplos.append(ord(m[i])+ord(m[i+1])+ord(m[i+2]))
    
    return anagramas_triplos

main()
