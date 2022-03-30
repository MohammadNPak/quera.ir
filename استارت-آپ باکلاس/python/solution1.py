# https://quera.org/problemset/10326/

w = [int(x) for x in input().split()]
person = [0]*4
n=0
while 0 not in w:
  person[n%4]+=1
  if (n%4)%2==0:
    w[0]-=1
  else:
    w[2]-=1
  n+=1
print(*person)
