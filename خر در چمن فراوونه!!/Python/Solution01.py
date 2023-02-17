a = int(input())
b = int(input())
l = int(input())
s = a
for i in range(1, l):
    if i % 2 != 0:
        s += b
    elif i % 2 == 0:
        s += a

print(s)
