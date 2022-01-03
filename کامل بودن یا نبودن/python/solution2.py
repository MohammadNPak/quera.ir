# https://quera.ir/problemset/282/

N = int(input())

counter = 1
s = 0
while counter < N:
    if N % counter == 0:
        s += counter
    counter += 1

if s == N:
    print("YES")
else:
    print("NO")