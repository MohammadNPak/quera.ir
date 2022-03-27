# https://quera.org/problemset/33045/
from math import sqrt,ceil

n = int(input())
sum_of_values:int = 0
counter:int = 0
for i in range(1,n+1):
    upper_bound = sqrt(i)
    if upper_bound == int(upper_bound):
      counter+=1
      sum_of_values+=int(upper_bound)
    for j in range(1,ceil(upper_bound)):
      if (a:=divmod(i,j))[1]==0:
        counter +=2
        sum_of_values+= a[0]+j
print(counter,sum_of_values)
