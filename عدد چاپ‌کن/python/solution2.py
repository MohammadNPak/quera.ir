a = int(input("Enter the number: "))
for i in str(a):
    b = []
    print(f"{int(i)}: ",end = (""))
    if int(i) > 0 :
        for j in range(int(i)):
            b.append(i)
    elif int(i) == 0 :
        print()
    output = "".join(b)
    if int(i) > 0 :
        print(int(output))
