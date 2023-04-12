# https://quera.org/problemset/26651/
num,sum=int(input()),0
listtest1,listtest2=list(input().split()),list(input().split())
for i in range(num):
    sum+=(int(listtest1[i])*int(listtest2[i]))
print(sum)
