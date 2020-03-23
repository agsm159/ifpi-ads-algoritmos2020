#09.Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

n1 = int(input('Digite um número:'))

for n2 in range(2, n1):
    if n1 % n2 == 0:
        exit('Esse número não é primo.')

print('Esse número é primo.')
