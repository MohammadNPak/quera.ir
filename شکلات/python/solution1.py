# https://quera.org/problemset/146465/

inpt = input().split()
n, k = int(inpt[0]), int(inpt[1])

if n % k == 0: print('YES')
else: print('NO')