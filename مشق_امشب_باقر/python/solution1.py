degrees = input().split()
a = int(degrees[0])
b = int(degrees[1])
c = int(degrees[2])
if a!= 0 and b!= 0 and c!= 0 and a+b+c == 180:
    print("Yes")
else:
    print("No")