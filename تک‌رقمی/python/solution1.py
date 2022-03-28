# https://quera.org/problemset/3539/


n = input()
while len(n)!=1:
    s = 0
    for i in n:
        s+=int(i)
    n = str(s)
print(n)