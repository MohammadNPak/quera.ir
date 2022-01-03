

number = int(input())
all = 0
for i in range(1, number):
    if number % i == 0:
        all += i
if all == number:
    print("YES")
else:
    print("NO")