# https://quera.ir/problemset/66859/

n, b = input().split()
n = int(n)
b = int(b)
output = ""
if b > 10:
    base_letters = [str(i) for i in range(10)]
    base_letters.extend([chr(ord("A")+i) for i in range(b-10)])
else:
    base_letters = [str(i) for i in range(b)]

# print(base_letters)

# {key: value for (key, value) in zip(range(b), [])}
if n < b:
    print(base_letters[n])
else:
    while n >= b:
        mod = n % b
        output += base_letters[mod]
        n //= b
    output += base_letters[n]

    print(output[::-1])
