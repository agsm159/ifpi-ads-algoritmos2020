def main():

    s = str(input('Digite a string a ser analisada: '))

    print(camelcase(s))

def camelcase(s):
    cont = 1

    for i in s:
        n = ord(i)

        if maiusculo(n):
            cont += 1

    return cont


def maiusculo(n):
    if (n >= 65 and n <= 90):
        return True

    else:
        return False 


main()
