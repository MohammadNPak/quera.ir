n=int (input())
i=0
s=0
avalin=int(input())
while i<(n-1) :
    a=int(input())
    if avalin != a :
        s+=1
    avalin=a
    i+=1
    
print(s)