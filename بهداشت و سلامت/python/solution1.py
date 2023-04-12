# https://quera.org/problemset/51865/
x=int(input())
n=int(input())
if n==0 :
    print ("20")

elif n==7 :
    print(x)

else :
    x=(x-n)
    if x<0:
        print ("0")
    else:
        print (x)