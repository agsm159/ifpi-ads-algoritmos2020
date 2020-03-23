#02-1.Digite este exemplo em um script e teste-o.

def do_twice(a):
    a()
    a()

def print_twice():
    print('spam')

def main():
    do_twice(print_twice)

main()
