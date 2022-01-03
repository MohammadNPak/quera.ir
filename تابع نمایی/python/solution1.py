# https://quera.ir/problemset/297/


x = float(input())
n = int(input())

ex = 0
loop_element = 1
for i in range(1, n+1):
    ex += loop_element
    loop_element = loop_element*(x / i)
ex = round(ex, 3)
print(f"{ex:.3f}")