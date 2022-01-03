# https://quera.ir/problemset/593/

n = int(input())
m = n
# 234
# 100000 -1 = 99999

# digit1 =n % 10
# n //10
# digit2 = n%10
# n//10

digit_sum = 0
counter = 0
while counter < 5:
    digit_sum += n % 10
    n = n//10
    counter += 1

b = digit_sum


def is_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    else:
        return True


number = m+1
i = 0
while i < b:

    if is_prime(number):
        i += 1
        if i == b:
            print(number)
    number += 1
