#02-2.Altere do_twice para que receba dois argumentos, um objeto de função e um valor,
# e chame a função duas vezes, passando o valor como um argumento.

def do_twice (a):
    a()
    a()

def print_stonks():
    print('stonks')

def print_not_stonks():
    print('not stonks')

def main():
    do_twice(print_stonks)
    do_twice(print_not_stonks)

main()
