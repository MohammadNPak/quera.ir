# https://quera.org/problemset/31025/


from math import floor
n,k =[int(x) for x in input().split()]
print(floor(n/(2**k)))