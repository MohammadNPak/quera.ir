# https://quera.org/problemset/102250/
def find(num1, num2, num3):
    a = {1, 2, 3, 4}
    b = {num1, num2, num3}
    c = list(a-b)[0]
    return c
