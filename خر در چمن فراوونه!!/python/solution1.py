# https://quera.org/problemset/4065/

a,b,l = map(int,input().split())
s = a
for i in range(1, l):
    if i % 2 != 0:
        s += b
    elif i % 2 == 0:
        s += a

print(s)
