# https://quera.ir/problemset/280/

a = int(input())
b = int(input())
c = int(input())

if a!=0 and b!=0 and c!=0:
    if a**2==b**2+c**2 or b**2 == a**2 +c**2 or c**2==a**2+ b**2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
