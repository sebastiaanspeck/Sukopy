import string

field = [['.' for a in range(9)] for b in range(9)]


def menu():
    print("""  _____             _         _           
 / ____|           | |       | |          
| (___   _   _   __| |  ___  | | __ _   _ 
 \___ \ | | | | / _` | / _ \ | |/ /| | | |
 ____) || |_| || (_| || (_) ||   < | |_| |
|_____/  \__,_| \__,_| \___/ |_|\_\ \__,_|
                                          """)
    play()


def play():
    # while the field is not correct, give a new input:
    draw_field()
    while not check_field():
        print("Lets Play...")
        get_input()
        draw_field()
    print("You won")


def get_input():
    while True:
        coordinates = input(str("Give the coordinates and your number (e.a. A5=7): "))
        if len(coordinates) < 3:
            print("You didn't entered enough input, give the input like A5=7")
            continue
        if ord(coordinates[0].upper()) - 65 <= 9 or int(coordinates[1]) - 1 < 9 or int(coordinates[3]) < 9:
            try:
                x = ord(coordinates[0].upper()) - 65
                y = int(coordinates[1]) - 1
                number = int(coordinates[3])
                field[x][y] = number
            except ValueError:
                print("You entered incorrect input, let's try again")
                continue
            break
            

def draw_field():
    print_x()
    print_y()


def print_x():
    print('  ', end='')
    for i in range(1, 10):
        if i % 3 == 0:
            print(i, end='   ')
        else:
            print(i, end=' ')
    print()


def print_y():
    for i in range(9):
        print(string.ascii_uppercase[i], end=' ')
        print_field(i)
        if i == 2 or i == 5:
            print("\n  ------+-------+------")
        else:
            print()
    print()


def print_field(i):
    for idex in range(9):
        if idex == 2 or idex == 5:
            print(field[i][idex], ' |', sep='', end=' ')
        else:
            print(field[i][idex], sep='', end=' ')


def check_field():
    # check if each square contains the numbers 1 to 9 only once.
    if not check_squares(a=0, b=3):
        return False
    # check if each row (A1 to A9) contains the numbers 1 to 9 only once.
    if not check_rows():
        return False
    # check if each column (A1 to I1) contains the numbers 1 to 9 only once.
    if not check_colums():
        return False
    return True


def check_squares(a, b):
    c = a
    d = b
    for x in range(1, 10):
        block = []
        for i in range(a, b):
            for j in range(c, d):
                block.append(field[i][j])
        if not set(block) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False
        c += 3
        d += 3
        if x % 3 == 0:
            a += 3
            b += 3
            c = 0
            d = 3


def check_rows():
    for x in range(9):
        block = field[x]
        if not set(block) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False


def check_colums():
    for x in range(9):
        block = []
        for i in range(9):
            block.append(field[i][x])
        if not set(block) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False


menu()
