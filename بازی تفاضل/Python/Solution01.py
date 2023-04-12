resault = 0


def game(number):
    a = number // 10
    b = number % 10
    if a > b:
        resault = a - b
    elif b > a:
        resault = b - a
    else:
        resault = 0
    print(resault)


game(int(input()))
