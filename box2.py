def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_eight(f):
    do_four(f)
    do_four(f)	

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_four(print_beam)
    print('+')

def print_posts():
    do_four(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_four(print_row)
    print_beams()

print_grid()
