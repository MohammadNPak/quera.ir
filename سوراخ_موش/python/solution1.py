x = input().split()
mouse = int(x[0])
hole = int(x[1])
if mouse == hole:
    print("Saal Noo Mobarak!")
else:
    if mouse > hole:
        for i in range((mouse-hole)):
            print("L", end="")
    else:
        for i in range((hole-mouse)):
            print("R", end="")
print()