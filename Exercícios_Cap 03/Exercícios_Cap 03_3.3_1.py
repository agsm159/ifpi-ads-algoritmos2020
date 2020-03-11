def do_twice(a):
    a()
    a()

def do_four(a):
    do_twice(a)
    do_twice(a)

def print_x():
    print('+ - - - -',end = ' ')

def print_y():
    print('|        ',end = ' ')

def print_q():
    do_twice(print_x)
    print('+')

def print_w():
    do_twice(print_y)
    print('|')

def print_e():
    print_q()
    do_four(print_w)

def main():
    do_twice(print_e)
    print_q()

main()


