def main():
    hexadecimal(decimal(binario()))
    
def binario():
    n = []
    for i in range(0, 8, 1):
        n.append(int(input("Digite o número em binário, um de cada vez: ")))
        print(n[i])

        if n[i] == 0 or n[i] == 1:
            print()
        else:
            print("Número Binário Inválido, Tente Inserir Somente Valores 0 ou 1") 
            break
    return n

def decimal(binario):
    j = 0
    decimal = 0
    for i in binario:
       decimal += i * (2 ** (len(binario)-(j+1)))
       j += 1
    print(decimal)
    return decimal

def hexadecimal(decimal):
    hexadecimal = []
    hexa = ""
    while decimal >= 16:
        hexadecimal.append(decimal % 16)
        decimal = decimal // 16
    hexadecimal.append(decimal)
    hexadecimal.reverse()
    for i in hexadecimal:
        if i >= 10:
            if i == 10:
                hexa += "A"
            elif i == 11:
                hexa += "B"
            elif i == 12:
                hexa += "C"
            elif i == 13:
                hexa += "D"
            elif i == 14:
                hexa += "E"
            elif i == 15:
                hexa += "F"
        else:
            hexa += str(i)
    print(hexa)

main()
