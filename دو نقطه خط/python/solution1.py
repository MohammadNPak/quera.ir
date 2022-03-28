# https://quera.org/problemset/3414/


x1,y1,x2,y2 = input().split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

if x1 == x2:
    print("Vertical")
elif y1==y2:
    print("Horizontal")
else:
    print("Try again")