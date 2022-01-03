# https://quera.ir/problemset/618/
n = int(input())


for i in range(2*n+1):
    for j in range(2*n+1):
        if i <= n:
            if j < (n-i):
                print(" ", end="")
            elif (n-i) <= j <= n+i:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j < i-n:
                print(" ", end="")
            elif j < 3*n-i+1:
                print("*", end="")
            else:
                print(" ", end="")
    print("")
