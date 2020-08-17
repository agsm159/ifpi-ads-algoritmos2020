def main():
    
    n = int(input('Digite um valor da sequência: '))

    termo = 1
    razao = 1

    while n >= razao:
        print(termo)

        razao = razao + 1
        termo = termo + razao
    
        
main()
