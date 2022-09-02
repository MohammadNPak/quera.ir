# https://quera.org/problemset/66867/

from functools import reduce
n,m = input().split()
n,m = int(n),int(m)

colors = []
for _ in range(m):
    colors.append(input())

is_even = reduce(
    lambda x,y:[ a ^ True if b=="W" else a  for a,b in zip(x,y)],
    colors,
    [True for _ in range(n)])

print(''.join(map(lambda x:"B" if x else "F",is_even)))