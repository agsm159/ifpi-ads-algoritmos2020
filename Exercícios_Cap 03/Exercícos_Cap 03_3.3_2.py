def do_twice(a):
    a()
    a()

def do_four(a):
    do_twice(a)
    do_twice(a)

def print_x():
    print(2 * '+ - - - -',end = ' ')

def print_y():
    print(2 * '|        ',end = ' ')

def print_z():
    do_twice(print_x)
    print('+')

def print_delta():
    do_twice(print_y)
    print('|')

def print_beta():
    print_z()
    do_four(print_delta)

def print_alfa():
    do_four(print_beta)
    print_z()

def main():
    print_alfa()

main()
