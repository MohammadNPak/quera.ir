nums = []
while True:
    num = input()
    if num != "0":
        nums.append(num)
    else:
        break
k = len(nums)-1
while k >= 0:
    print(nums[k])
    k-=1