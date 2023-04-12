# https://quera.org/problemset/80651/
a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())
a3=int(input())
b3=int(input())

min1=a1
if b1<a1 :
    min1=b1

min2=a2
if b2<a2 :
    min2=b2

min3=a3
if b3<a3 :
    min3=b3

print(min1+min2+min3)