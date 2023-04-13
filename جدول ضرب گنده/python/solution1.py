# https://quera.org/problemset/3409/
x = int(input())
for i in range(1, x+1):
    print('\n')
    for j in range(1, x+1):
        print(f'{i*j}', end=' ')
