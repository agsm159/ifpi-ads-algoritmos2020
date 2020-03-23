#02-5.Defina uma função nova chamada do_four que receba um objeto de função e um valor e chame a função quatro vezes,
# passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.

def do_four(a):
    a()
    a()
    a()
    a()

def print_four():
    print('spam')
    print('spam')

def main():
    do_four(print_four)

main()
