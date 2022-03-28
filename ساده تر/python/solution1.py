# https://quera.org/problemset/3403/

numbers = []
for i in range(4):
    numbers.append(int(input()))

Product = 1
for number in  numbers:
    Product*=number

print(f"""Sum : {sum(numbers):.6f}
Average : {sum(numbers)/len(numbers):.6f}
Product : {Product:.6f}
MAX : {max(numbers):.6f}
MIN : {min(numbers):.6f}""")
