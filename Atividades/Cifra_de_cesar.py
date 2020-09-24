def main():

    rotações = int(input('Digite a quantidade de rotaçãoes:'))
    string = str(input('Digite a palavra ou letra desejada para rotacionar: '))

    rotate_world(rotações, string)

def rotate_world(x, world):

    for i in world:
        rot = ord(i)
        
        if (rot >= 65) and (rot <= 90):
            rot = rot + x
            
            if rot <= 90:
                print(chr(rot))

            elif rot > 90:
                rot = (rot - 90) + 64
                print(chr(rot))

        elif (rot >= 97) and (rot <= 122):
            rot = rot + x

            if rot <= 122:
                print(chr(rot))

            elif rot > 122:
                rot = (rot - 122) + 96
                print(chr(rot))

            

main()
