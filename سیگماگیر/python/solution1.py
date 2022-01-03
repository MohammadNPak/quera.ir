# https://quera.ir/problemset/647/

n = int(input())
m = int(input())

sigma = 0
for i in range(-10, m+1):
    for j in range(1, n+1):
        sigma = sigma + int((i+j)**3/(j**2))
print(sigma)