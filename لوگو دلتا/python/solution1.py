n = int(input())
for i in range(n-1):
    for j in range(2*n-1):
        if n-1-i == j or n-1+i==j:
            print('D',end="")  
        else:
            print('.',end='')
    print()
for j in range(2*n-1):
    if j%2==0:
        print('D',end="")  
    else:
        print('.',end='')
        