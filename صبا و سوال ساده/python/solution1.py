# https://quera.org/problemset/31025/

from math import floor
n,k = input().split()
n,k = int(n),int(k)

for i in range(k):
    n=n/2

print(floor(n))