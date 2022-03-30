# https://quera.org/problemset/3540/

n,x,y = map(int,input().split())
# ax+by=n => a = (n-by)/x  => a must be an integer
b=0
while b*y <= n:
  if (n-b*y)%x==0:
    print((n-b*y)//x,b)
    break
  b+=1
else:
  print(-1)
