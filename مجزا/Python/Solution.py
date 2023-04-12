integers = []
EvenNums = []
OddNums = []


def separator():
    for i in range(0, 10):
        integers.append(int(input()))

    for item in integers:
        if item % 2 == 0:
            EvenNums.append(item)
        elif item % 2 != 0:
            OddNums.append(item)

    return (EvenNums, OddNums)


x = separator()
print(x)
