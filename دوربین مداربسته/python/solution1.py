# https://quera.org/problemset/2794/


x1,y1 = [int(x) for x in input().split()]
x2,y2 = [int(x) for x in input().split()]
x3,y3 = [int(x) for x in input().split()]

if x1 == x2:
    if y3 ==y1:
        print(x3,y2)
    elif y3==y2:
        print(x3,y1)
elif x2 ==x3:
    if y1 == y2:
        print(x1,y3)
    elif y1== y3:
        print(x1,y2)
elif x3==x1:
    if y2==y1:
        print(x2,y3)
    elif y2==y3:
        print(x2,y1)

