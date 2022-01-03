# https://quera.ir/problemset/589/


def factorial(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f

m = int(input())
k = factorial(m)
print(k)