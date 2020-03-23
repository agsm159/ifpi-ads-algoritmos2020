#02-4.Use a versão alterada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento.

def do_twice (a):
    a()
    a()

def print_twice():
    print('spam')

def main():
    do_twice(print_twice)
    do_twice(print_twice)

main()
