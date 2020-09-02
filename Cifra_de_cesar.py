def main():

    rotações = int(input('Digite a quantidade de rotaçãoes:'))
    string = str(input('Digite a palavra ou letra desejada para rotacionar: '))

    rotate_world(rotações, string)

def rotate_world(x, world):

    for i in world:
        rot = ord(i)
        rot = rot + x

        print(chr(rot))


main()
