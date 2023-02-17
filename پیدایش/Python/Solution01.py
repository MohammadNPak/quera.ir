resault = 0


def find(num1, num2, num3):
    nums = str(num1) + str(num2) + str(num3)
    f1 = nums.find('1')
    f2 = nums.find('2')
    f3 = nums.find('3')
    f4 = nums.find('4')
    if f1 == -1:
        resault = 1
    elif f2 == -1:
        resault = 2
    elif f3 == -1:
        resault = 3
    elif f4 == -1:
        resault = 4
    print(resault)


find(input(), input(), input())
