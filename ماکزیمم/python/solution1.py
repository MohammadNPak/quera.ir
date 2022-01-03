# https://quera.ir/problemset/588/

_ = int(input())
numbers = input().split()

for i in range(len(numbers)):
    numbers[i]= int(numbers[i])

max_value = numbers[0]
for index in range(len(numbers)):
    if max_value < numbers[index]:
        max_value = numbers[index]

print(max_value)